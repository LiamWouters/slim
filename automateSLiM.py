import json
import subprocess, argparse, os

## Script Arguments ##
parser = argparse.ArgumentParser(prog="automateSLiM.py", description="This program allows a user to run a .slim simulation file multiple times.")

# Input .slim file to run
parser.add_argument("-f", "--file", action="store", help="Specify input simulation file (.slim)", required=True)
# Input .json file to extract script parameters from
parser.add_argument("-c", "--config", action="store", help="Specify input configuration file (.json)")
# Number of simulations ran
parser.add_argument("-n", action="store", help="Specify how many times to run the simulation, default is 10")
# Output file
parser.add_argument("-o", "--output", action="store", help="Specify output file for simulation logs, default is log.txt")
# std out
parser.add_argument("--std-out", action="store_true", help="Print output in console instead of output file")

args = parser.parse_args()

NUM_SIMULATIONS = args.n or 10
if type(NUM_SIMULATIONS) == str:
    NUM_SIMULATIONS = int(NUM_SIMULATIONS)
OUTPUT_FILE = "./output_logs/" + (args.output or "log.txt")
INPUT_FILE = args.file
INPUT_CONFIG = args.config or None


## Error handling
if ".slim" not in INPUT_FILE:
    raise ValueError("Input file given is not a .slim file")

if not os.path.isdir("./output_logs"):
    os.mkdir("./output_logs")
    
if os.path.isfile(OUTPUT_FILE) and not args.std_out:
    print(f"WARNING: file {OUTPUT_FILE} already exists.")
    user_input = input("Overwrite file Y/N? ")
    if user_input == "y" or user_input == "Y":
        print("Overwriting file")
        # Clear contents
        f = open(OUTPUT_FILE, 'w').close()
    else:
        exit("Stopping")


## extra functions
def writeOutput(output: str, prefix: str = ""):
    if args.std_out:
        print(prefix + output)
        return
    
    f = open(OUTPUT_FILE, "a")
    f.write(prefix + output)
    f.close()


## Read configuration ##
if INPUT_CONFIG:
    slim_program = ["slim"]
    with open(INPUT_CONFIG) as file:
        config: dict = json.loads(file.read())
        if config.get("count"):
            NUM_SIMULATIONS = config["count"]
        if config.get("variables"):
            for var in config["variables"].keys():
                if config["variables"][var]["type"] == "list":
                    for i in config["variables"][var]["values"]:
                        slim_program.append("-d")
                        slim_program.append(f"{var}={i}")
                elif config["variables"][var]["type"] == "range":
                    for i in range(config["variables"][var]["start"], config["variables"][var]["end"],
                                   config["variables"][var]["step"]):
                        slim_program.append("-d")
                        slim_program.append(f"{var}={i}")
    slim_program.append(INPUT_FILE)
else:
    slim_program = ["slim", INPUT_FILE]

output_log = ""


## Run Simulations ##
try:
    print("running simulations...")
    
    for i in range(NUM_SIMULATIONS):
        print("simulation: ", i+1)
        arguments = [(arg[(i % len(arg))] if isinstance(arg, list) else arg) for arg in slim_program]
        result = subprocess.run(arguments, capture_output=True)
        writeOutput(str(result.stdout, encoding="utf-8"), f"--> Simulation {i+1}\n")
    
    print("finished simulations")
    
except FileNotFoundError:
    raise SystemError("'slim' is not installed or cannot be found")

except Exception as e:
    print("Failed to run simulations")
    print("error:", e)
