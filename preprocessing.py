#this file does all the important data preprocessing

import preprocessing_functions as func

def main():
    max_length = 15000
    all_x, all_y, names = func.populate_lists()

    all_x = func.padding_x(all_x, max_length)

    all_x = func.alter_spike(all_x, 100, 1.50)

    all_x, all_y, names = func.shuffle(all_x, all_y, names)

    train_x, val_x, test_x, train_y, val_y, test_y = func.split(all_x, all_y, 0.15, 0.15)

    train_x, scaler = func.standardize_all(train_x, max_length)
    val_x = func.standardize_all(val_x, max_length, scaler)
    test_x = func.standardize_all(test_x, max_length, scaler)
    
    #other scaling techniques:
    # train_x, scaler = func.normalize_all(train_x, max_length)
    # val_x = func.normalize_all(val_x, max_length, scaler)
    # test_x = func.normalize_all(test_x, max_length, scaler)

    # train_x = func.standardize_each(train_x)
    # val_x = func.standardize_each(val_x)
    # test_x = func.standardize_each(test_x)    

    # train_x = func.normalize_each(train_x)
    # val_x = func.normalize_each(val_x)
    # test_x = func.normalize_each(test_x)

    # possible duplication and reshuffling
    # train_x, test_x, train_y, test_y = func.duplicate(train_x, test_x, train_y, test_y, 2)
    # train_x, test_x, train_y, test_y, names = func.shuffle([train_x, test_x, train_y, test_y, names])

    train_x, val_x, test_x, train_y, val_y, test_y = func.array_and_reshape(train_x, val_x, test_x, train_y, val_y, test_y, max_length)

    #need to save the pickle objects for future use
    func.to_pickle(train_x, val_x, test_x, train_y, val_y, test_y)
    # print(names[0])
    # print(names[1])

    func.scaler_to_pickle(scaler)

    func.move_test(test_x, test_y, names)


if __name__ == "__main__":
    main()


