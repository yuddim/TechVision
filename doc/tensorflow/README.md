# Документация по работе с библиотекой [TensorFlow](https://www.tensorflow.org/)

# Содержание
+ [Установка и настройка](#install)
 + [Установка TensorFlow](#TensorFlow)
   + [Linux(Ubuntu)](#install_Linux)
   + [Windows](#install_Windows)
 + [Установка OpenCV](#openCV)
   + [Linux(Ubuntu)](#lin_opencv)
   + [Windows](#WinCV)
+ [Скользящее окно](#slidingWindow)
+ [Демо пример](#demo)

# <a name="install"></a> Установка и настройка


## <a name="TensorFlow"></a> Установка TensorFlow
### <a name="install_Linux"></a> Linux(Ubuntu)
Перед установкой tensorFlow нам необходимо произвести настройки и обновление пакетов.
Для этого мы открываем терминал (Ctr+Alt+T - по умолчанию). В открывшейся консоли выполним:

     $ sudo apt-get install python-pip python-dev
мы установим пакетный менеджер pip для python и сам интерпретатор.
Затем дождемся зовершения установки  и выполним в консоли установку tensorflow:

     $ pip install tensorflow
Для установки версии tensorFlow для gpu:

    $ pip install tensorflow-gpu

В случае если данные команды завершились с ошибками, тогда:

    # Ubuntu/Linux 64-bit, CPU only, Python 2.7
    $ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.1-cp27-none-linux_x86_64.whl

    # Ubuntu/Linux 64-bit, GPU enabled, Python 2.7
    # Requires CUDA toolkit 8.0 and CuDNN v5. For other versions, see "Installing from sources" below.
    $ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-0.12.1-cp27-none-linux_x86_64.whl

    # Ubuntu/Linux 64-bit, CPU only, Python 3.4
    $ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.1-cp34-cp34m-linux_x86_64.whl

    # Ubuntu/Linux 64-bit, GPU enabled, Python 3.4
    # Requires CUDA toolkit 8.0 and CuDNN v5. For other versions, see "Installing from sources" below.
    $ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-0.12.1-cp34-cp34m-linux_x86_64.whl

    # Ubuntu/Linux 64-bit, CPU only, Python 3.5
    $ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.12.1-cp35-cp35m-linux_x86_64.whl

    # Ubuntu/Linux 64-bit, GPU enabled, Python 3.5
    # Requires CUDA toolkit 8.0 and CuDNN v5. For other versions, see "Installing from sources" below.
    $ export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_gpu-0.12.1-cp35-cp35m-linux_x86_64.whl

Затем сноваа попытаться установить:

    # Python 2
    $ sudo pip install --upgrade $TF_BINARY_URL

    # Python 3
    $ sudo pip3 install --upgrade $TF_BINARY_URL

В случае не удачи посетить [сайт библиотеки](https://www.tensorflow.org/get_started/os_setup)

Примеромом является выполнение команды _python_ в терминале. Откроется консоль интерпретатора
затем выполнить следующий скрипт:

    $ python

    >>> import tensorflow as tf
    >>> hello = tf.constant('Hello, TensorFlow!')
    >>> sess = tf.Session()
    >>> print(sess.run(hello))
    Hello, TensorFlow!
    >>> a = tf.constant(10)
    >>> b = tf.constant(32)
    >>> print(sess.run(a + b))
    42
    >>>

Установка завершена.

### <a name="install_Windows"></a> Windows
>Доработать инструкцию

## <a name="openCV"></a> Установка OpenCV
Для установке необходим Cmake.

Windows:

Скачать с [сайта](https://cmake.org/)  для своей платформы.

Linux (Ubuntu)
Скачать с [сайта](https://cmake.org/). sh - фаил затем например

    bash cmake-3.7.2-Linux-x86_64.sh или ./cmake-3.7.2-Linux-x86_64.sh

Возможно потребуются права супер пользователя.



### <a name="lin_opencv"></a> Linux(Ubuntu)
Открываем [оф. сайт OpenCV](http://opencv.org/downloads.html)
и выбираем версию 3.2. Скачиваем.

Переходим в каталог куда скачали распаковываем например в

    /home/user/
После распаковки выполняем

    cd ~/opencv && mkdir build && cd build
Затем:

### <a name="WinCV"></a> Windows

### <a name="slidingWindow"></a> Скользящее окно

### <a name="demo"></a> Пример
