def is_user_auth():
    return False


def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        if is_user_auth():
            print('User is authenticated!')
            return fn(*args, **kwargs)
        else:
            raise Exception('User is NOT authenticated!')

    return wrapper


@check_user_auth
def do_sensitive_job():
    print('Results of sensitive job: ...')


try:
    do_sensitive_job()
except Exception as e:
    print(e)
