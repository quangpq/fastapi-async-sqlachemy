import os

import uvicorn

if __name__ == "__main__":
    # Use for debug only
    os.environ['TZ'] = 'Europe/London'
    log_config = uvicorn.config.LOGGING_CONFIG
    log_config["formatters"]["access"]["fmt"] = "%(asctime)s %(levelname)s: %(message)s"
    log_config["formatters"]["default"]["fmt"] = "%(asctime)s %(levelname)s: %(message)s"
    uvicorn.run("app.main:app", host="0.0.0.0", port=5000, reload=True, log_config=log_config)
