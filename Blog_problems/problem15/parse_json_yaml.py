#work in progress
import json
import yaml

def main():

	json_file = open("ip.json")

	data = json.load(json_file)
	print("\nJSON\n")
	print(data)
	json_file.close()

	yaml_file = open("ip.yaml")

	data = yaml.load(yaml_file)
	print("\nYAML\n")
	print(data)
	yaml_file.close()


if __name__ =="__main__":
	main()