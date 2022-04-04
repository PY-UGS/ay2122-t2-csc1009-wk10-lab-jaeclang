'''
Lab 10 QN.3 
Done By: 1802965
'''
def descending_order():
	for each_num in range(101,66,-2):
		print(each_num)


def module_info():
	module_code = "CSC1009"

	'''
	'match' requires python version 3.10 and above
		- I utilized a dictionary instead, Key-Value pairs
	'''
	# match module_code:
	# 	case "CSC1006":
	# 		return("Mathematics II")
	# 	case "CSC1008":
	# 		return("Data Structures & Algorithm")
	# 	case "CSC1009":
	# 		return("Object-Oriented Programming")
	# 	case "CSC2902":
	# 		return("Career & Professional Development")
	# 	case _:
	# 		return("Invalid Module Code")

	module_dict = {
		"CSC1006" : "Mathmematics II",
		"CSC1008" : "Data Structures Algorithm",
		"CSC1009" : "Object-Oriented Programming",
		"CSC2902" : "Career & Professional Development"
	}
	return(module_dict[module_code])	# Returns Value that belongs to the Module Code


def main():
	print(module_info())
	descending_order()


if __name__ == '__main__':
	main()