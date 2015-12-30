import filecmp

FILE1 = 'backupn148.pkl'
FILE2 = 'backupn149.pkl'

print ('Files {} {} are equal?'.format(FILE1, FILE2), filecmp.cmp(FILE1, FILE2))
