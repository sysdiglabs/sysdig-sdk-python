import json
import os
import tempfile

from expects import expect, have_key, have_keys, contain, equal, start_with
from expects.matchers.built_in import be_false, be_empty
from mamba import before, it, context, after, description

from sdcclient.monitor import DashboardsClientV2
from specs import be_successful_api_call

_DASHBOARD_NAME = "test_dashboard_ci"

with description("Dashboards v2", "integration") as self:
    with before.all:
        self.client = DashboardsClientV2(sdc_url=os.getenv("SDC_MONITOR_URL", "https://app.sysdigcloud.com"),
                                         token=os.getenv("SDC_MONITOR_TOKEN"))

    with before.each:
        self.cleanup_test_dashboards()

    with after.each:
        self.cleanup_test_dashboards()


    def cleanup_test_dashboards(self):
        ok, res = self.client.get_dashboards()
        expect((ok, res)).to(be_successful_api_call)

        for dashboard in res["dashboards"]:
            if str(dashboard["name"]).startswith(_DASHBOARD_NAME):
                call = self.client.delete_dashboard(dashboard)
                expect(call).to(be_successful_api_call)


    def create_test_dashboard(self):
        ok, res = self.client.create_dashboard(name=_DASHBOARD_NAME)
        if ok:
            self.test_dashboard = res["dashboard"]

        return ok, res


    with it("is able to create a dashboard with just a name"):
        ok, res = self.client.create_dashboard(name=_DASHBOARD_NAME)
        expect((ok, res)).to(be_successful_api_call)
        expect(res).to(have_key("dashboard"))

    with it("is able to create a dashboard from a file"):
        self.create_test_dashboard()
        with tempfile.NamedTemporaryFile(mode="w+") as f:
            # Write the info to the temp file
            json.dump({"dashboard": self.test_dashboard, "version": "v2"}, f)
            f.flush()
            f.seek(0)

            ok, res = self.client.create_dashboard_from_file(dashboard_name=f"{_DASHBOARD_NAME}_2", filename=f.name,
                                                             filter=None)
            expect((ok, res)).to(be_successful_api_call)

    with it("is able to create a dashboard from a view"):
        _, res_view_list = self.client.get_views_list()

        call = self.client.create_dashboard_from_view(newdashname=f"{_DASHBOARD_NAME}_2",
                                                      viewname=res_view_list["defaultDashboards"][0]["name"],
                                                      filter=None)
        expect(call).to(be_successful_api_call)

    with context("when there are existing dashbords"):
        with before.each:
            self.create_test_dashboard()

        with it("is able to list all the dashboards"):
            ok, res = self.client.get_dashboards()
            expect((ok, res)).to(be_successful_api_call)
            expect(res).to(have_key("dashboards", contain(have_keys("name", "id"))))

        with it("is able to retrieve the test dashboard by its id"):
            ok, res = self.client.get_dashboard(dashboard_id=self.test_dashboard["id"])
            expect((ok, res)).to(be_successful_api_call)
            expect(res).to(have_key("dashboard", have_keys("name", id=equal(self.test_dashboard["id"]))))

        with context("when deleting a dashboard"):
            with it("is able to remove it if all the info provided is correct"):
                _, res = self.client.get_dashboards()
                dashboard_len_before = len(res["dashboards"])

                call = self.client.delete_dashboard(self.test_dashboard)

                _, res = self.client.get_dashboards()
                dashboard_len_after = len(res["dashboards"])

                expect(call).to(be_successful_api_call)
                expect(dashboard_len_after).to(equal(dashboard_len_before - 1))

            with it("fails to delete it if the info provided is not correct"):
                ok, res = self.client.delete_dashboard({"id": 0})
                expect(ok).to(be_false)
                expect(res).to(equal("status code 404"))

            with it("returns an error if there is not 'id' field in the provided object"):
                ok, res = self.client.delete_dashboard({})

                expect(ok).to(be_false)
                expect(res).to(equal("Invalid dashboard format"))

        with it("is able to dump the dashboard to a file"):
            with tempfile.NamedTemporaryFile(mode="w+") as f:
                self.client.save_dashboard_to_file(dashboard=self.test_dashboard, filename=f.name)
                f.flush()
                f.seek(0)

                data = json.load(f)
                expect(data).to(have_keys(version=equal("v2"), dashboard=equal(self.test_dashboard)))

        with it("is able to create a dashboard from template"):
            call = self.client.create_dashboard_from_template(dashboard_name=f"{_DASHBOARD_NAME}_2",
                                                              template=self.test_dashboard,
                                                              scope='agent.id = "foo"')
            expect(call).to(be_successful_api_call)

        with context("when it's created with an incorrect scope"):
            with it("fails if the scope is not a string"):
                ok, res = self.client.create_dashboard_from_template(dashboard_name=f"{_DASHBOARD_NAME}_2",
                                                                     template=self.test_dashboard,
                                                                     scope={})
                expect(ok).to(be_false)
                expect(res).to(equal("Invalid scope format: Expected a string"))

            with it("fails if the scope has incorrect format"):
                ok, res = self.client.create_dashboard_from_template(dashboard_name=f"{_DASHBOARD_NAME}_2",
                                                                     template=self.test_dashboard,
                                                                     scope="foobarbaz")
                expect(ok).to(be_false)
                expect(res).to(start_with("invalid scope: foobarbaz"))

        with it("is able to create a dashboard from a configuration"):
            self.test_dashboard["name"] = f"{_DASHBOARD_NAME}_2"
            call = self.client.create_dashboard_with_configuration(self.test_dashboard)

            expect(call).to(be_successful_api_call)

        with context("when creating a dashboard from other dashboard"):
            with it("creates the dashboard correctly if the template exists"):
                ok, res = self.client.create_dashboard_from_dashboard(newdashname=f"{_DASHBOARD_NAME}_2",
                                                                      templatename=_DASHBOARD_NAME, filter=None)
                expect((ok, res)).to(be_successful_api_call)

            with it("returns an error saying the dashboard does not exist"):
                ok, res = self.client.create_dashboard_from_dashboard(newdashname=f"{_DASHBOARD_NAME}_2",
                                                                      templatename="NonExistingDashboard", filter=None)
                expect(ok).to(be_false)
                expect(res).to(equal("can't find dashboard NonExistingDashboard to use as a template"))

        with it("is able to update a dashboard"):
            self.test_dashboard["name"] = f"{_DASHBOARD_NAME}_updated"
            call = self.client.update_dashboard(self.test_dashboard)

            expect(call).to(be_successful_api_call)

        with it("is able to retrieve the dashboard by it's name"):
            ok, res = self.client.find_dashboard_by(name=self.test_dashboard["name"])

            expect((ok, res)).to(be_successful_api_call)
            expect(res).to(contain(
                have_key("dashboard", have_keys(id=self.test_dashboard["id"], name=self.test_dashboard["name"])))
            )
