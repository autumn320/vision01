import cv2
img = cv2.imread(r"D:\vision01\images\test.jpg")

if img is None:
    print("读取失败：图片路径不对，或者文件不存在")
else:
    # 打印图片尺寸：高度 宽度 通道数
    print("图片尺寸：", img.shape)

    # 在窗口里显示
    cv2.imshow("test", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(r"D:\vision01\out\test.jpg",img)
