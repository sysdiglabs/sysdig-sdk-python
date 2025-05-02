import os
from random import choice
from string import ascii_letters

from expects import expect, contain
from mamba import before, description, after, it, context

from sdcclient import SdcClient
from specs import be_successful_api_call

with description("User Provisioning", "integration") as self:
    with before.each:
        self.client = SdcClient(
            sdc_url=os.getenv("SDC_MONITOR_URL", "https://app.sysdigcloud.com"),
            token=os.getenv("SDC_MONITOR_TOKEN"),
        )
        self.user_name = "terraform-test+user@sysdig.com"

    with after.each:
        self.client.delete_user(self.user_name)

    with it("is able to provision the user with only the username"):
        ok, res = self.client.create_user(self.user_name)
        expect((ok, res)).to(be_successful_api_call)

    with it("is able to provision the user with name and lastname"):
        ok, res = self.client.create_user(self.user_name, "Name", "LastName")
        expect((ok, res)).to(be_successful_api_call)

    with it("is able to provision the user with password"):
        random_password = "".join(choice(ascii_letters) for _ in range(20))
        ok, res = self.client.create_user(self.user_name, password=random_password)
        expect((ok, res)).to(be_successful_api_call)

    with it("is able to provision the user with name, lastname and password"):
        random_password = "".join(choice(ascii_letters) for _ in range(20))
        ok, res = self.client.create_user(
            self.user_name, "Name", "LastName", random_password
        )
        expect((ok, res)).to(be_successful_api_call)

    with context("when the customer already exists"):
        with it("returns an error saying it already exists"):
            ok, res = self.client.create_user(self.user_name)
            expect((ok, res)).to(be_successful_api_call)

            ok, res = self.client.create_user(self.user_name)
            expect((ok, res)).not_to(be_successful_api_call)
            expect(res).to(contain(f"User {self.user_name} already exists"))
