from base import HttpClient
from tasks import TasksClient
from workflows import WorkflowsClient

from jeeves_commons.constants import DEFAULT_REST_PORT


class JeevesClient(object):
    def __init__(self, host='localhost', port=DEFAULT_REST_PORT, headers={},
                 username=None, password=None):
        url = 'http://{0}:{1}/api/v1.0/'.format(host, port)
        self.api = HttpClient(endpoint_url=url,
                              username=username,
                              password=password,
                              headers=headers)

        self.tasks = TasksClient(self.api)
        self.workflows = WorkflowsClient(self.api)


# import yaml
# client = JeevesClient()
# wf_path = '/home/adaml/dev/jeeves-minion/resources/examples/' \
#           'jeeves_workflow.yaml'
# with open(wf_path) as f:
#     workflow = yaml.load(f)
# res, stat = client.workflows.upload(workflow, {}, workflow_id='testing')
#
# pass
#
# lst_res, lst_stat = client.workflows.list()
