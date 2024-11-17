# 使用说明

## 前提条件

在开始之前，请确保您已经完成了外部工程的配置、编译和安装。可以通过运行以下脚本来完成：

```bash
./build.sh
```

## 进入 Examples 目录

在完成外部工程的安装后，进入 `examples` 目录：

```bash
cd examples
```

## 调用外部生成的库

在 `examples` 目录中，您可以看到如何调用外部生成的库。以下是一个简单的示例：

```bash
./build.sh
```

## 发布者和订阅者的使用

### 发布者

以下是一个发布者的示例代码：

```cpp
// - create talker node
Node node("talker");
// - create publisher
Publisher<std_msgs::String>::Ptr pub =
    node.Advertise<std_msgs::String>("topic_color", 1);
// - create rate
Rate rate(1);
while (Ok()) {
  // - create message
  std_msgs::String msg;
  msg.data = "red";
  // - publish message
  pub->Publish(msg);
  std::cout << "I say: " << msg.data << std::endl;
  rate.Sleep();
}
```

### 订阅者

以下是一个订阅者的示例代码：

```cpp
// - create listener node
Node node("listener");
// - subscrib topic_difference
Subscriber<std_msgs::String>::Ptr sub =
    node.Subscribe<std_msgs::String>("topic_color", 1, Callback);
// - spin
Spin();
```
### 启动
```bash
# 开启core
cd ../build && ./hlbcore
# 开启终端启动node
cd build && ./talker
# 开启终端启动node
cd build && ./listener
```

通过以上示例，您可以了解如何在 `examples` 目录中调用外部生成的库，并基于它们实现发布者和订阅者的功能。