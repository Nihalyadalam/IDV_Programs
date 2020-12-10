import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import collections

data_array = []
field = []
img_format = []
img_count = 500


# Function for calculating Arithmetic Mean
def calculate_mean(data):
    _total = sum(data)
    _mean = _total/len(data)
    return _mean


# Function for calculating variance
def calculate_variance(data, average):
    _variance = sum((val - average) ** 2 for val in data) / len(data)
    return _variance


# Plotting histogram
def plot_histogram():
    data_frames = pd.read_csv("i170b2h0_t0.txt", quotechar='"', header=None)
    input_array = np.array(data_frames)
    plt.title('Histogram for Band 2')
    plt.xlabel('X-axis: number of values', fontsize=11)
    plt.ylabel('Y-axis: occurrences of values', fontsize=11)
    plt.hist(input_array, histtype="step")
    plt.savefig("Histogram_band_2.png")
    plt.show()
    plt.clf()


# Reading the file
def file_read_band_2():
    f = open("i170b2h0_t0.txt", "r")

    for element in f:
        element = element.split(",")
        r_element = element
        r_element.reverse()
        r_element[0] = r_element[0].strip('\n')
        r_element.reverse()
        field.append(r_element)

    for i in range(img_count-1, -1, -1):
        img_format.append(field[i])

    for i in range(0, img_count):
        for j in range(0, img_count):
            img_format[i][j] = img_format[i][j].replace('"', '')
            img_format[i][j] = (float(img_format[i][j]))
            data_array.append(img_format[i][j])

    return data_array


# Plotting Non-Linear Transformed Image
def non_linear_transformation():

    for i in range(0, img_count-1):
        for j in range(0, img_count-1):
            img_format[i][j] = np.log((img_format[i][j]))

    plt.imshow(img_format, cmap='gray')
    plt.xlabel('X-axis', fontsize=11)
    plt.ylabel('Y-axis', fontsize=11)
    plt.title("Non-Linear Transformation")
    color_bar = plt.colorbar()
    color_bar.set_ticks([np.min(img_format), np.max(img_format)])
    color_bar.set_ticklabels(["low", "high"])
    color_bar.ax.set_ylabel('Intensity', fontsize=11)
    plt.savefig("Non-LinearTrans_band_2.png")
    plt.title('Non Linear Transformation Band 2')
    plt.show()
    plt.clf()


# Drawing profile line
def draw_profile_line_band_2(file_data):
    print(np.size(file_data))
    max_index = np.where(file_data == np.amax(file_data))
    prof_line_data_x = np.reshape(file_data, (img_count, img_count))
    plt.plot(prof_line_data_x[67])
    plt.xlabel('X-axis values', fontsize=11)
    plt.ylabel('Y-axis values', fontsize=11)
    plt.title("Profile line for the max element of the data set")
    plt.savefig("profile_line_band_2.png")
    plt.show()
    plt.clf()


# Histogram equalization for Band 1
def histogram_equ_band_1():

    hist_equ_mat_1 = get_hist_data("i170b1h0_t0.txt")
    plt.xlabel('X-axis', fontsize=11)
    plt.ylabel('Y-axis', fontsize=11)
    plt.title("Histogram-Equalization-Band1")
    plt.imshow(hist_equ_mat_1, cmap="gray")
    color_bar = plt.colorbar()
    color_bar.set_ticks([np.min(hist_equ_mat_1), np.max(hist_equ_mat_1)])
    color_bar.set_ticklabels(["low", "high"])
    color_bar.ax.set_ylabel('Intensity', fontsize=11)
    plt.savefig("Histogram-Equalization-Band1.png")
    plt.show()
    plt.clf()
    return hist_equ_mat_1


# Histogram equalization for Band 2
def histogram_equ_band_2():

    hist_equ_mat_2 = get_hist_data("i170b2h0_t0.txt")
    plt.xlabel('X-axis', fontsize=11)
    plt.ylabel('Y-axis', fontsize=11)
    plt.title("Histogram-Equalization-Band2")
    plt.imshow(hist_equ_mat_2, cmap="gray")
    color_bar = plt.colorbar()
    color_bar.set_ticks([np.min(hist_equ_mat_2), np.max(hist_equ_mat_2)])
    color_bar.set_ticklabels(["low", "high"])
    color_bar.ax.set_ylabel('Intensity', fontsize=11)
    plt.savefig("Histogram-Equalization-Band2.png")
    plt.show()
    plt.clf()
    return hist_equ_mat_2


# Histogram equalization for Band 3
def histogram_equ_band_3():

    hist_equ_mat_3 = get_hist_data("i170b3h0_t0.txt")
    plt.xlabel('X-axis', fontsize=11)
    plt.ylabel('Y-axis', fontsize=11)
    plt.title("Histogram-Equalization-Band3")
    plt.imshow(hist_equ_mat_3, cmap="gray")
    color_bar = plt.colorbar()
    color_bar.set_ticks([np.min(hist_equ_mat_3), np.max(hist_equ_mat_3)])
    color_bar.set_ticklabels(["low", "high"])
    color_bar.ax.set_ylabel('Intensity', fontsize=11)
    plt.savefig("Histogram-Equalization-Band3.png")
    plt.show()
    plt.clf()
    return hist_equ_mat_3


# Histogram equalization for Band 4
def histogram_equ_band_4():

    hist_equ_mat_4 = get_hist_data("i170b4h0_t0.txt")
    plt.xlabel('X-axis', fontsize=11)
    plt.ylabel('Y-axis', fontsize=11)
    plt.title("Histogram-Equalization-Band4")
    plt.imshow(hist_equ_mat_4, cmap="gray")
    color_bar = plt.colorbar()
    color_bar.set_ticks([np.min(hist_equ_mat_4), np.max(hist_equ_mat_4)])
    color_bar.set_ticklabels(["low", "high"])
    color_bar.ax.set_ylabel('Intensity', fontsize=11)
    plt.savefig("Histogram-Equalization-Band4.png")
    plt.show()
    plt.clf()
    return hist_equ_mat_4


# Getting Histogram Data for each band
def get_hist_data(file):

    f = open(file, "r")

    field = []
    image_data = []
    data_array = []
    c_data = []
    p_data = []
    my_dict = {}
    cdf = 0

    for element in f:
        element = element.split(",")
        r_element = element
        r_element.reverse()
        r_element[0] = r_element[0].strip('\n')
        r_element.reverse()
        field.append(r_element)

    for i in range(img_count-1, -1, -1):
        image_data.append(field[i])

    for i in range(0, img_count):
        for j in range(0, img_count):
            image_data[i][j] = image_data[i][j].replace('"', '')
            image_data[i][j] = (float(image_data[i][j]))
            data_array.append(image_data[i][j])

    hist_mat = image_data

    data_array.sort()

    for x in data_array:
        if x not in c_data:
            c_data.append(x)

    freq_dict = collections.Counter(data_array)

    for aKey in freq_dict:
        my_dict[aKey] = freq_dict[aKey];

    for key in my_dict:
        p_data.append(my_dict.get(key))
        p = my_dict.get(key)
        pr = my_dict.get(key) / img_count * img_count
        cdf += pr
        s = cdf * 255
        my_dict[key] = s

    for i in range(0, img_count):
        for j in range(0, img_count):
            value = my_dict.get(image_data[i][j])
            hist_mat[i][j] = value

    return hist_mat


# Scaling 0 to 255
def scale_255(image_data):

    linear_data = np.array(image_data)
    linear_flat = linear_data.flatten()
    linear_trans = []

    r_min = min(linear_flat)
    r_max = max(linear_flat)
    s_max = 255

    for element in linear_flat:
        l_value = int((element - r_min) / (r_max - r_min) * s_max)
        linear_trans.append(l_value)

    linear_shape = np.reshape(linear_trans, (500, 500, 3))
    return linear_shape


# Create an RGB image
def rgb_image(hist_equ_mat_4, hist_equ_mat_3, hist_equ_mat_1):
    rgb = []
    rgb = hist_equ_mat_4
    rgbArray = []

    for i in range(0, img_count):
        for j in range(0, img_count):
            red = (int(hist_equ_mat_4[i][j]))
            green = (int(hist_equ_mat_3[i][j]))
            blue = (int(hist_equ_mat_1[i][j]))
            color = []
            color.append(red)
            color.append(green)
            color.append(blue)
            rgb[i][j] = color

    scale_rgb = scale_255(rgb)
    print(np.shape(scale_rgb))

    plt.imshow(scale_rgb)
    plt.xlabel('X-axis', fontsize=11)
    plt.ylabel('Y-axis', fontsize=11)
    plt.title("RGB Image")
    color_bar = plt.colorbar()
    color_bar.set_ticks([np.min(scale_rgb), np.max(scale_rgb)])
    color_bar.set_ticklabels([np.min(scale_rgb), np.max(scale_rgb)])
    color_bar.ax.set_ylabel('Intensity', fontsize=11)
    plt.savefig("RGB-Image.png")
    plt.show()
    plt.clf()


# Main function
def main():
    file_data = file_read_band_2()
    mean = calculate_mean(file_data)
    print("Mean: ", mean)
    variance = np.var(data_array)
    print("Variance: ", variance)
    max_data = np.max(data_array)
    print("Max Data: ", max_data)
    min_data = np.min(data_array)
    print("Min Data: ", min_data)
    draw_profile_line_band_2(file_data)
    plot_histogram()
    non_linear_transformation()
    hist_equ_mat_1 = histogram_equ_band_1()
    hist_equ_mat_2 = histogram_equ_band_2()
    hist_equ_mat_3 = histogram_equ_band_3()
    hist_equ_mat_4 = histogram_equ_band_4()

    print(np.shape(hist_equ_mat_1))
    print(np.shape(hist_equ_mat_2))
    print(np.shape(hist_equ_mat_3))
    print(np.shape(hist_equ_mat_4))

    rgb_image(hist_equ_mat_4, hist_equ_mat_3, hist_equ_mat_1)


if __name__ == "__main__":
    main()