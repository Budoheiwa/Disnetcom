



def copy_lines(input_file_name, output_file_name1, output_file_name2, output_file_name3, output_file_name4, keywords1, keywords2, keywords3, keywords4):
    with open(input_file_name, 'r') as input_file, open(output_file_name1, 'w') as output_file1, open(output_file_name2, 'w') as output_file2, open(output_file_name3, 'w') as output_file3, open(output_file_name4, 'w') as output_file4:
        for line in input_file:
            if any(motclé in line for motclé in keywords1):
                output_file1.write(line)
            if any(motclé in line for motclé in keywords2):
                output_file2.write(line)
            if any(motclé in line for motclé in keywords3):
                output_file3.write(line)
            if any(motclé in line for motclé in keywords4):
                output_file4.write(line)


input_file_name = 'testread.txt'
output_file_name1 = 'nom_fichier_user.txt'
output_file_name2 = 'nom_fichier_banane.txt'
output_file_name3 = 'nom_fichier_pwd.txt'
output_file_name4 = 'nom_fichier_cigarette.txt'

keyword_group_1 = ['user', 'utilisateur']
keyword_group_2 = ['banane']
keyword_group_3 = ['password', 'pwd', 'mot de passe']
keyword_group_4 = ['cigarette']

copy_lines(input_file_name, output_file_name1, output_file_name2, output_file_name3, output_file_name4, keyword_group_1, keyword_group_2, keyword_group_3, keyword_group_4)
