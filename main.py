import sys, getopt
from code_generator import final_code

def main(argv):
    inputfile = ''
    outputfile = ''
    code = ""
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('main.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    with open("tests/" + inputfile, "r") as input_file:
        code = input_file.read().strip()
        code = final_code(code)

    with open("out/" + outputfile, "w") as output_file:
        # write result to output file. 
        # for the sake of testing :
        output_file.write(code)


if __name__ == "__main__":
    main(sys.argv[1:])
