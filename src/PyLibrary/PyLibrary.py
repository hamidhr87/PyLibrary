import requests

class PyLibrary:
    def __init__(self, username, password) -> None:
        self._agent_url = "http://154.91.170.22:30001"
        self.username = username
        self.password = password
        self._token = self._get_token(self.username, self.password)

    def _get_token(self, username, password):
        payload = {}
        headers = {}
        ulr_with_parameters = f"{self._agent_url}/user/get_token?username={username}&password={password}"
        response = requests.request("GET", ulr_with_parameters, headers=headers, data=payload)
        return response.text

    def upload_file(self, bucket_name, bucket_type, domain_name, file_path):
        ulr_with_parameters = f"{self._agent_url}/datasource/upload_objects"
        payload = {
            'name': 'test',
            'type': 'bucket',
            'domain_name': 'domain1'
        }
        files = [
            ('file', (
                'Pond_new.json',
                open(file_path, 'rb'),
                'application/json'
            ))
        ]
        headers = {
            'Authorization': f'Bearer {self._token}'
        }

        response = requests.request(
            "POST", ulr_with_parameters, headers=headers, data=payload, files=files)
        print(response.text)

    def download_file(self, bucket_name, domain_name, file_name):
        url = f"{self._agent_url}/datasource/download_bucket_objects?name={bucket_name}&domain_name={domain_name}&object_name={file_name}"
        payload = {}
        headers = {
            'Authorization': f'Bearer {self._token}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text)


obj = PyLibrary("f.taheri", "1234")
