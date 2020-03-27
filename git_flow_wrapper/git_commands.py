import subprocess


def __run(args: str):
    """
    Runs git commands
    :param args: any git param
    :return: system call result
    """
    stdout = subprocess.check_output(["git"] + args.split())
    return stdout.decode()


def _list_merged_branchs():
    """
    List merged branchs
    :return:
    """
    out = __run("branch --no-color --merged")
    return [
        b.strip("* ")
        for b in out.splitlines()
        if b.strip("* ") not in ("master", "develop")
    ]


def _delete_branch(name: str):
    __run(f"branch -d {name}")


def _delete_merged_branchs():
    for branch in _list_merged_branchs():
        _delete_branch(branch)


def _fetch_remote_changes():
    __run("fetch --all")


def _get_current_branch():
    out = __run("branch --show-current")
    return out.strip()


def create_new_feature(name: str):
    __run("checkout develop")
    __run("pull origin develop")
    _fetch_remote_changes()
    _delete_merged_branchs()
    __run(f"flow feature start {name}")
    return _get_current_branch()


def create_new_hotfix(name: str):
    __run("checkout master")
    __run("pull origin master")
    _fetch_remote_changes()
    _delete_merged_branchs()
    __run(f"flow hotfix start {name}")
    return _get_current_branch()


def create_new_release(version: str):
    name = f"v{version.replace('v', '')}"
    __run("checkout develop")
    __run("pull origin develop")
    _fetch_remote_changes()
    _delete_merged_branchs()
    __run(f"flow release start {name}")
    return _get_current_branch()


def publish_remote():
    current_branch = _get_current_branch()
    __run(f"push origin {current_branch}")
    return current_branch
