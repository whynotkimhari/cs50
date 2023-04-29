Hi, my name is Bui Nguyen Kim Hai. I am from Vietnam. My english may not good, i am sorry for that. I am trying to learn it to use it more naturally.
_______________________________________________________________

In this project, I have tried to experiment with some sort of training and preparing data for training.
+ First of all that is load_data function. In this function, at first tries, I did not understand what this function does, and then I split it to 10 epochs which each of them just have 60 - not 500 as example. After reading "Specification" some numbers of time then I realized that I needed to use np.array, resize the img, divide it by 255.0 and category it. 

+ The next thing is get_model function. In spite of watching the lecture very hard, but I could not actually understand what to do in this step. Then I moved to the "Source Code" to review it. And I did find out what to do, I called it "the form" of code. Based on that some lines of code, I can write my own with my own optimization. Let's dive in what I have did.
    + At first, I rewrite all the code from Source Code and run to see any bug going to happen. And Voila, the code run successfully.
    + Then, I try to add some hidden layers with 4, 12 and 32 nodes. It really seems quite good.
    + The next day, I read more hard the Source Code and watch again some peaks in the lecture. So I went to my code and add convolutional, pooling layers and flatten it. It did run well. But this time, I have noticed more about the corrective rate, then I change the numbers of nodes in hidden layers to 128 and then 256. Add some dropout layers to ensure that the neural network will work well with different data sets. 
    + The output layer is the layer that I did not modify too many times. I just modified it 2 times. Switching it between "sigmoid" and "softmax" to see what is more suitable with my code.
    + The last thing is model compile, I choose to use the compile as the one in the Source Code use.

After many times optimizing the code, my neural network sometimes give the high accuracy, sometimes low. Sometimes it takes too long to training, sometimes not. But I believe that my code here is acceptable because the loss is low and the accuracy is kind of high. After this project, I have learn more about AI and how we actually use python library such as Tensorflow to train neural network.

Thanks for teaching!