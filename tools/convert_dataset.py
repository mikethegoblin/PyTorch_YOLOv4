import glob, os

# Current directory
current_dir = os.getcwd()

print(current_dir)

train_dir = '/coco/images/train2017'
val_dir = '/coco/images/val2017'
test_dir = '/coco/images/test2017'

file_train = open('coco/train2017.txt', 'w')
file_val = open('coco/val2017.txt', 'w')
file_test = open('coco/test.txt', 'w')


for filepath in glob.iglob(os.path.join(current_dir+train_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(filepath))
    file_train.write('coco/images/train2017/' + title + '.jpg' + '\n')

for filepath in glob.iglob(os.path.join(current_dir+val_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(filepath))
    file_val.write('coco/images/val2017/' + title + '.jpg' + '\n')

for filepath in glob.iglob(os.path.join(current_dir+test_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(filepath))
    file_test.write('coco/images/test2017/' + title + '.jpg' + '\n')

# close files
file_train.close()
file_val.close()
file_test.close()