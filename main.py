from image import *

def main():
    img = "Text.jfif"
    img = checkFormat(img)
    img = resize(img, hight=720, width=500)

    thresh = Threshold(img)

    data = loadData(thresh)
    print(data)


    showImg(thresh)


if __name__ == "__main__":
    main()
