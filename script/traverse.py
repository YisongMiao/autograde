import os
import shutil
import regex as re
from pathlib import Path


def traverse(save_dir, desired_fname):
    Path(save_dir).mkdir(parents=True, exist_ok=True)

    rootDir = '../data/cs4248-a1'
    for dirName, subdirList, fileList in os.walk(rootDir):
        # print('Found directory: {}'.format(dirName))
        # print('Found file: {}'.format(fileList))
        pass

    for fname in fileList:
        # Copied from ../data/cs4248-a1/A0000001L(Steve Jobs)(1).zip to ../data/cs4248-a1/A00000001L.zip
        if re.search(r'\(1\)', fname):
            matric_num = re.findall(r'A[0-9]+[A-Z]', fname)[0]
            src = rootDir + '/' + fname
            dst = rootDir + '/' + matric_num + '.zip'
            shutil.copy(src, dst)
            print('Copied from {} to {}'.format(src, dst))

    valid_count = 0
    for fname in fileList:
        if re.search(r'A[0-9]+[A-Z].zip', fname):
            valid_count += 1
            matric_num = re.findall(r'A[0-9]+[A-Z]', fname)[0]
            src = rootDir + '/' + fname
            dst = rootDir + '/' + matric_num
            shutil.unpack_archive(src, dst)
            print('Unzipped from {} to {}'.format(src, dst))
    print('Unzipped number is: {}'.format(valid_count))

    copy_count = 0
    for dirName, subdirList, fileList in os.walk(rootDir):
        # print('---')
        # print('Found directory: {}'.format(dirName))
        # print('Found file: {}'.format(fileList))

        # if re.search(r'%s' % desired_fname, f):
        #     if re.search(r'maxos', f) or re.search(r'MAXOS', f):
        #         continue
        for f in fileList:
            if f == desired_fname:
                src = dirName + '/' + f
                matric_num = re.findall(r'A[0-9]+[A-Z]', src)[0]
                dst = save_dir + '/' + matric_num + '.py'
                shutil.copy(src, dst)
                copy_count += 1
                # print('Copied from {} to {}'.format(src, dst))
    print('Copied number is {}'.format(copy_count))


if __name__ == '__main__':
    traverse('../data/Q1', 'obj1_tokenizer.py')
    traverse('../data/Q2', 'obj2_edit_distace.py')
    traverse('../data/Q2', 'obj2_edit_distance.py')  # Out typo. Students corrected.
    traverse('../data/Q3', 'obj3_sentiment.py')
    traverse('../data/Q4', 'obj4_ngram_lm.py')

    print('done')
