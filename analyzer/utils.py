import cv2
from celery import shared_task


@shared_task
def canbeinpdf(img_w, img_h, canvas_w, canvas_h):
    """
        This function permits to know if the image
        can be on pdf.

        img_w  (int): Image's width
        img_h  (int): Image's height
        canvas_w  (int): Pdf's width
        canvas_h  (int): Pdf's height
        Return:
        bool: true if the image is smaller or equal than pdf's size
    """
    if img_w <= canvas_w and img_h <= canvas_h:
        return True
    return False


@shared_task
def getOrientiation(image_obj):
    """
        This function permits get the image's orientation.
        Parameters:
        image_obj  (image): Image to analyze
        Return:
        str: horizontal ar vertical orientation
    """
    high, width = image_obj.shape[:2]
    orientation = width/high
    if orientation >=1:
        return 'horizontal'
    else:
        return 'vertical'


@shared_task
def analyzeVerticalImage(image_obj, canvas_width, canvas_height, scale_w=99, scale_h=99):
    """
        This function permits analyze and return the image'size correct for pdf's size
        for a vertical orientation

        img_w  (int): Image's width
        img_h  (int): Image's height
        canvas_w  (int): Pdf's width
        canvas_h  (int): Pdf's height
        scale_w (int): porcent of width to resize image
        scale_h (int): porcent of height to resize image
        Return:
        [string, int, int]: image's orientation, image's width, image's height
    """
    height_img, width_img = image_obj.shape[:2]

    while not canbeinpdf(width_img, height_img, canvas_width, canvas_height):
        new_h = int(height_img * scale_h / 100)
        new_w = int(canvas_width * scale_w / 100)
        image_new = cv2.resize(image_obj, (new_w, new_h), interpolation=cv2.INTER_AREA)
        height_img, width_img = image_new.shape[:2]
        scale_w = scale_w - 2
        scale_h = scale_h - 1

    return width_img, height_img


@shared_task
def analyzeHorizontalImage(image_obj, canvas_width, canvas_height, scale_w=99, scale_h=99):
    """
        This function permits analyze and return the image'size correct for pdf's size
        for a horizontal orientation

        img_w  (int): Image's width
        img_h  (int): Image's height
        canvas_w  (int): Pdf's width
        canvas_h  (int): Pdf's height
        scale_w (int): porcent of width to resize image
        scale_h (int): porcent of height to resize image
        Return:
        [string, int, int]: image's orientation, image's width, image's height
    """
    height_img, width_img = image_obj.shape[:2]

    while not canbeinpdf(width_img, height_img, canvas_width, canvas_height):
        new_h = int(height_img * scale_h /100)
        new_w = int(canvas_width * scale_w /100)
        image_new = cv2.resize(image_obj, (new_w, new_h), interpolation=cv2.INTER_AREA)
        height_img, width_img = image_new.shape[:2]
        scale_w = scale_w - 1
        scale_h = scale_h - 2

    return width_img, height_img



