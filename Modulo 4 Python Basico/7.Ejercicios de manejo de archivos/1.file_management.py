def get_files(sorted_song_list):

    path_first_file = 'Song List1.txt'
    with open(path_first_file, encoding='utf-8') as file:
        for line in file.readlines():
            sorted_song_list.append(line)



            
    sorted_song_list = sorted(sorted_song_list)
    print(f'{sorted_song_list}')

    return sorted_song_list




def main():
    # path = 'Tareas\\manejo de datos\\file 1.txt'
    sorted_song_list = []
    path_second_file = 'SortedList.txt'
    sortedList = get_files(sorted_song_list)
    
    with open(path_second_file, 'w', encoding='utf-8') as file:
        for i in sortedList:
            file.write(i)


    print(f'{sortedList}')
    
    

if __name__ == "__main__":
    main()