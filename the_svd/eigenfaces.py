
def main():
    img_list = []
    for i in range(20):
        fpath = 'resources/faces/img%02d.png' %i
        img_list.append(color2gray(file2image(fpath)))
    centroid = [[sum(img_list[i][r][c] for i in range(20))
                 for 

if __name__ == '__main__':
    main()
