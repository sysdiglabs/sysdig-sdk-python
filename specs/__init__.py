from expects.matchers import Matcher


class _BeSuccessfulApiCall(Matcher):
    def _match(self, expect):
        ok, result = expect
        if ok:
            return True, [f"the api call was successful: {str(result)}"]
        return False, [f"the result is {str(result)}"]


be_successful_api_call = _BeSuccessfulApiCall()
