arr = [64, 25, 12, 22, 11]

# For rotate,
# 1. normalize first by module with array length,
# 2. then for right, reverse array, Reverse first k, then reverse rest n - k
# 3. for left, reverse first k, then reverse rest n - k, then reverse whole array


def rotate_array(arr, by, direction):
    print("Input Array : ", end=str(arr) + "\n")
    shifts = by % len(arr)
    print("Normalized Shift by :", str(shifts), direction)

    match direction:
        case "right":
            arr.reverse()
            first_half = arr[:shifts]
            second_half = arr[shifts:]
            first_half.reverse()
            second_half.reverse()
            return first_half + second_half

        case "left":
            first_half = arr[:shifts]
            second_half = arr[shifts:]
            first_half.reverse()
            second_half.reverse()
            final_arr = first_half + second_half
            final_arr.reverse()
            return final_arr

        case _:
            raise Exception(f"Invalid rotate direction ! Wtf is : {direction}")


print(rotate_array(arr, 6, "right"))