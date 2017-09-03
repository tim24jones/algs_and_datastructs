class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

def read_file(filename):
    htmldoc=open("filename","r")
    file_str=htmldoc.read()
    tag_stack=Stack()
    for char in file_str:
        if char=='<':
            list=[]
            if file_str[char+1]=='/':
                while i in file_str[char+i]!=('>'or '/'):
                    list.append(file_str[char+i])
                    endtag=pop(tag_stack)
                    if endtag!=list:
                       return 'Error with tag',list
            else:
                while i in file_str[char+i]!='>':
                    list.append(file_str[char+i])
                    empty_element=['area','base','br','col','hr','img','input','link','meta','param','command','keygen','source']
                    if list not in empty_element:
                        push(tag_stack,list)
            char=char+i
        if not isEmpty(tag_stack):
            return 'Error, unclosed tags'
        else:
            return 'No tag errors found'
    htmldoc.close()
