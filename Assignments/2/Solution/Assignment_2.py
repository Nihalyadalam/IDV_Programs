import numpy as np
import matplotlib.pyplot as plt

# Arrays declarations
file_data = []
linear_trans = []
non_linear_trans = []


# Function for calculating Arithmetic Mean
def calculate_mean(data):
    _total = sum(data)
    _mean = _total/len(data)
    return _mean


# Function for calculating variance
def calculate_variance(data, average):
    _variance = sum((val - average) ** 2 for val in data) / len(data)
    return _variance


# File-open and read operation of a .raw file
def file_read():
    f = open("slice150.raw", "rb")
    file_data_raw = np.fromfile(f, dtype=np.int16)
    return file_data_raw


# Plotting profile line for the 256th element
def plot_profile_line(file_data_2d):
    prof_line_data_x = file_data_2d[255]
    plt.plot(prof_line_data_x)
    plt.xlabel('X-Axis', fontsize=11)
    plt.ylabel('Y-Axis', fontsize=11)
    plt.title("Profile line for the 256th element of the data set")
    plt.margins(x=0)
    plt.savefig("profile_line_scan.jpg")
    plt.show()
    plt.clf()


# Plotting histogram
def plot_histogram(image_data):
    values, occur = np.unique(image_data, return_counts=True)
    plt.plot(values, occur)
    plt.xlabel('Occurrences', fontsize=11)
    plt.ylabel('Values', fontsize=11)
    plt.title("Histogram as a Line-Graph")
    plt.savefig("histogram_line.jpg")
    plt.show()
    plt.clf()


# Linear Transformation
def linear_transformation(image_data):
    r_min = min(image_data)
    r_max = max(image_data)
    s_max = 255

    for element in image_data:
        l_value = int((element - r_min)/(r_max - r_min) * s_max)
        linear_trans.append(l_value)

    linear_trans_s = np.reshape(linear_trans, (512, 512))
    # Plotting Linear Transformed Image
    plt.imshow(linear_trans_s, cmap='gray')
    plt.xlabel('X-Axis', fontsize=11)
    plt.ylabel('Y-Axis', fontsize=11)
    plt.title("Linear Transformation")
    color_bar = plt.colorbar()
    color_bar.set_ticks([np.min(linear_trans), np.max(linear_trans)])
    color_bar.set_ticklabels(["low", "high"])
    color_bar.ax.set_ylabel('Color scale', fontsize=10)
    plt.savefig("LinearTrans.jpg")
    plt.show()
    plt.clf()


# Non-Linear Transformation (log (N+1))
def non_linear_transformation(image_data):
    for element in image_data:
        value = np.log(element + 1)
        non_linear_trans.append(value)

    non_linear_trans_s = np.reshape(non_linear_trans, (512, 512))

    # Plotting Non-Linear Transformed Image
    plt.imshow(non_linear_trans_s, cmap='gray')
    plt.xlabel('X-Axis', fontsize=11)
    plt.ylabel('Y-Axis', fontsize=11)
    plt.title("Non-Linear Transformation using Log2(N+1)")
    color_bar = plt.colorbar()
    color_bar.set_ticks([np.min(non_linear_trans), np.max(non_linear_trans)])
    color_bar.set_ticklabels(["low", "high"])
    color_bar.ax.set_ylabel('Color scale', fontsize=10)
    plt.savefig("Non-LinearTrans.jpg")
    plt.show()
    plt.clf()


# Implementation of box-car smoothing filter
def box_car_smoothing_filter(image_data):

    print(np.shape(image_data))
    print(range(0, len(image_data)-10))
    box_car_img = []
    for l in range(0, len(image_data)-10):
        for k in range(0, len(image_data)-10):
            total = 0
            for i in range(l, l + 11):
                for j in range(k, k + 11):
                    total += image_data[i][j]
            total = total / 121
            box_car_img.append(total)

    box_car_img_s = np.reshape(box_car_img, (502, 502))
    # Plotting Non-Linear Transformed Image
    plt.imshow(box_car_img_s, cmap='gray')
    plt.xlabel('X-Axis', fontsize=11)
    plt.ylabel('Y-Axis', fontsize=11)
    plt.title("Box-car smoothing filter")
    color_bar = plt.colorbar()
    color_bar.set_ticks([np.min(box_car_img), np.max(box_car_img)])
    color_bar.set_ticklabels(["low", "high"])
    color_bar.ax.set_ylabel('Color scale', fontsize=10)
    plt.savefig("Box-car smoothing filter.jpg")
    plt.show()
    plt.clf()


def main():
    image_data = file_read()
    file_data_2d = np.reshape(image_data, (512, 512))
    print(file_data_2d)
    plot_profile_line(file_data_2d)
    mean = calculate_mean(image_data)
    print("Mean: ", mean)
    variance = calculate_variance(image_data, mean)
    print("Variance: ", variance)
    plot_histogram(image_data)
    linear_transformation(image_data)
    non_linear_transformation(image_data)
    box_car_smoothing_filter(file_data_2d)


if __name__ == "__main__":
    main()
