import os
import shutil

import normalize

def collect_fileinfos(path_directory):
    all_types = []
    arch_files = []
    doc_files = []
    filesurvey = []
    img_files = []
    music_files = []
    video_files = []
    unknown_format = []
    new_name=''
    type=''
    main_dir=path_directory
    def dir_work(path_directory, main_dir):
        content_dir = os.listdir(path_directory)
        if '.DS_Store' in content_dir: content_dir.remove('.DS_Store')
        for filename in content_dir:
            path_file = os.sep.join([path_directory, filename])
            nor_name = normalize.normalize(filename)
            if os.path.isdir(path_file):
                dir_work(path_file, main_dir)
                if len(os.listdir(path_file)) == 0:
                    print(len(os.listdir(path_file)))
                    os.rmdir(path_file)
            else:
                filesurvey.append((path_directory, filename))
                type = os.path.splitext(filename)[-1]
                all_types.append(type)
                if type in ['.jpeg', '.png', '.jpg', '.svg']:
                    directory = os.sep.join([main_dir, 'images'])
                    if not os.path.exists(directory): os.makedirs(directory)
                    shutil.move(path_file, (f'{directory}' + f'/{nor_name}'))
                    img_files.append(nor_name)
                if type in ['.avi', '.mp4', '.mov', '.mkv']:
                    directory = os.sep.join([main_dir, 'videos'])
                    if not os.path.exists(directory): os.makedirs(directory)
                    shutil.move(path_file, (f'{directory}' + f'/{nor_name}'))
                    video_files.append(nor_name)
                if type in ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']:
                    directory = os.sep.join([main_dir, 'documents'])
                    if not os.path.exists(directory): os.makedirs(directory)
                    shutil.move(path_file, (f'{directory}' + f'/{nor_name}'))
                    doc_files.append(nor_name)
                if type in ['.mp3', '.ogg', '.wav', '.amr']:
                    directory = os.sep.join([main_dir, 'audio'])
                    if not os.path.exists(directory): os.makedirs(directory)
                    shutil.move(path_file, (f'{directory}' + f'/{nor_name}'))
                    music_files.append(nor_name)
                if type in ['.zip', '.gz', '.tar']:
                    directory = os.sep.join([main_dir, 'archives'])
                    if not os.path.exists(directory): os.makedirs(directory)
                    shutil.move(path_file, (f'{directory}' + f'/{nor_name}'))
                    new_name=os.path.splitext(nor_name)[0]
                    ar_dir = f'{directory}'+f'/{new_name}'
                    if not os.path.exists(ar_dir): os.makedirs(ar_dir)
                    shutil.unpack_archive((f'{directory}' + f'/{nor_name}'), ar_dir)
                    arch_files.append(nor_name)
                if type in ['.wenb', '.webm', '.sql', '', '.crdownload'] or type == [] or type is None:
                    shutil.move(path_file, (f'{main_dir}' + f'/{nor_name}'))
                    unknown_format.append(type)
    dir_work(path_directory, main_dir)
    print(f'arch_files {arch_files}')
    print(f'doc_files {doc_files}')
    print(f'img_files {img_files}')
    print(f'music_files {music_files}')
    print(f'video_files {video_files}')
    print(f'all_types {all_types}')
    print(f'unknown_format {unknown_format}')
    
    if __name__ == '__main__':
        collect_fileinfos()


