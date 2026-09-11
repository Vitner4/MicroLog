from microlog import Logger

log = Logger()

print("\n--- Basic logging ---")
log.info("Good!")
log.warning("Look out!")
log.error("Error!!!")

print("\n--- Disable logging ---")
log.disable()
log.info("This should not appear")

print("\n--- Enable logging ---")
log.enable()
log.info("Logging enabled again")

print("\n--- Custom log path ---")
log.path = "./test_microlog.log"
log.info("Writing to custom file")


