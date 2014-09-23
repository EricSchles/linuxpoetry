from buildbot.process.factory import BuildFactory
from buildbot.steps.shell import ShellCommand


ansiblerun = ShellCommand(
    name="ansible run",
    command=[
        "/var/projects/poetry/venvs/current/bin/ansible",
        "-c",
        "local /var/projects/poetry/code/current/deployment"],
    description="run local provisioning with ansible."
)

f_simplebuild = BuildFactory()
f_simplebuild.addStep(ansiblerun)

c = {}
c['builders'] = [
    BuilderConfig(name="simplebuild", slavenames=['slave1'], factory=f_simplebuild)
]
