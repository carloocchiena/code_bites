def retry(exception, max_tries=5):
    def retry_decorator(func):
        def _wrapper(*args, **kwargs):
            tries = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except exception as error:
                    tries += 1
                    if tries <= max_tries:
                        time.sleep(10)
                    else:
                        raise error
        return _wrapper
    return retry_decorator

@retry(Exception)
def may_fail():
    return go
  
