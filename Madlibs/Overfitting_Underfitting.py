def madlib():
    noun1 = input("Noun: ")
    verb1 = input("Verb: ")
    noun3= input("Noun: ")
    phenomenon_name = input("Noun: ")
    adj1=input("Adjective: ")
    second_phenonemon_name = input("Noun: ")


    madlib = f"When we divide the tree amongst many leaves, we also have fewer {1} in each leaf. \
             Leaves with very few houses will {2} predictions that are quite close to  actual values, \
             but they may make very unreliable {3} for new data (because each prediction is based on only a few houses). \
             This is a phenomenon called {phenomenon_name}, where a model matches the training data almost {adj1}, but does poorly in validation and other new data. \
             On the flip side, if we make our tree very shallow, it doesn't divide up the houses into very distinct groups. \
             At an extreme, if a tree divides houses into only 2 or 4, each group still has a wide variety of houses. \
             Resulting predictions may be far off for most houses, even in the training data (and it will be bad in validation too for the same reason). \
             When a model fails to capture important distinctions and patterns in the data, so it performs poorly even in training data, that is called {second_phenonemon_name}. \
             Since we care about accuracy on new data, which we estimate from our validation data, we want to find the sweet spot between underfitting and overfitting. \
             Visually, we want the low point of the (red) validation curve in the figure below."

    print(madlib)