import sys
import logging
import logging.handlers

log = logging.getLogger(__name__)

class capture_ut():
    def __init__(self):
        super().__init__()
        logging.info("test line1")

def capture_start(node_name, dal_name, filter, namespace, sut, username, capture_obj, capture_type):
    log.info("Starting capture" + capture_obj + " on node " + node_name + 
        "\n using " + capture_type + "\n filtered by " + filter)
    log.debug("test debug")
    log.warning("test warning")
    log.error("test error")
    if (dal_name):
        log.debug("currently on " + dal_name)
    else:
        log.error("Invalid Dal!")

def capture_stop():
    saved_paths = ["/lab/sandbox/euser/filename", "/lab/sandbox/euser/path2", "/lab/sandbox/euser/path3"]
    return saved_paths
