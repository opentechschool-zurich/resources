# Using Firebase from a Flutter app

This short tutorial extends the classical counter code by storing and retriving the value to and from Cloud Firestore.

In this tutoria, We will create an app for Android.

## Creating a Flutter project, a Firebase project and linking them together

First you can create a new Flutter project:

- You will need the package name later so pick a good one.
- If you're creating from the command line:  
  `flutter create --org com.yourdomain package_name`

Then you create a new Firebase project that will be bound to your app:

- Go to <https://firebase.google.com/>
- Create an account (if you don't have one yet)
- Create a new project
  - Name it `Counter`
  - Disable analytics
- Register the Android App
  - Click on the Android icon
  - Add the package name
    - It's in the first line of `android/app/src/main/AndroidManifest.xml`...
    - It's the value you have defined in the last step when creating the project with Android Studio and it looks like a reversed internet address (`com.example.myproject`).
    - If you you don't like the name, it's not easy to change it. You can grep for the current identifier, catch all occurrences...  but it might still fail. Since the project is still empty you'd probably better recreate a new one.
 - Register the app
 - Download the `google-service.json` file.

It's time to go back to the Flutter project and set it up for Firebase:

- Copy the `google-service.json` file you have downloaded into your projects `android/app`
- Add to `android/build.gradle` the line  
  `classpath 'com.google.gms:google-services:4.3.5'`  
  after the last `classpath` entry.  
  (you can [check here](https://developers.google.com/android/guides/google-services-plugin) which is the current version of the Goolge services plugin.)
- Add to the bottom of `android/app/build.gradle` the line  
  `apply plugin: 'com.google.gms.google-services'`.
- Add the `cloud_firestore` package to the dependencies in `pubspec.yaml`:  
  `cloud_firestore: ^1.0.1`  
    (You can check on the [package's page](https://pub.dev/packages/cloud_firestore) what is the current version.)
- In `android/app/build.gradle`, make sure that the minimal sdk is 21 (not the default 16)  
  (If you want to  support older Android versions, you need to add multidex (<https://stackoverflow.com/a/56368847/5239250>).)

([Firebase Tutorial for Flutter: Getting Started](https://www.raywenderlich.com/7426050-firebase-tutorial-for-flutter-getting-started) has nice screenshots that show well how to setup a Firestore document.)

## In Cloud Firestore Create a collection with a single document

In _Cloud Firestore_ web interface

- start a collection called `Counter`,
- with the single value called `value`
- of type `integer`, and
- with the initial value of `1`.
- Finally, let Firestore generate a Document ID (in my case it's `Qat49RJvyUkyWB48GWcK`).

## 

- Initialize flutterfire in the App
  - https://firebase.flutter.dev/docs/overview/#initializing-flutterfire

### Using a mostly synchronous approach

Our first approach will be, to simply get the current value from Firebase when the App starts.

Later, each time the `+` button is clicked, we will  store the new value into Firebase.

First we import `cloud_firestore` at the top of `lib/main.dart`:

```dart
import 'package:firebase_core/firebase_core.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
```

Then, we need to initialise Firebase: we do it in the `main()` function.  
We make `main()` `async`, wait for _everything_ being initialized, and then initialize Firebase:

```dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

As soon as the app is running, we want to set the counter to the value stored in Firebase.  
([What Does WidgetsFlutterBinding.ensureInitialized() do?](https://stackoverflow.com/questions/63873338/what-does-widgetsflutterbinding-ensureinitialized-do/63873689#63873689).)

In `__MyHomePageState` create an `initState()` function and check that it correctly gets called before `build()`:

```dart
  @override
  initState() {
    super.initState();
    _counter = 2;
  }
```

We let it set the counter value to `2` to have a visual change in the app.

We can now finish to implement `initState()` and get it to set the counter to the value stored in Firebase:

```dart
  @override
  initState() {
    super.initState();
    _counter = 0;

    FirebaseFirestore.instance
      .collection('Counter')
      .doc('Qtplxp4R9JyvUykW84WGcK')
      .get()
      .then((DocumentSnapshot documentSnapshot) {
        if (documentSnapshot.exists) {
          var data = documentSnapshot.data();
          // print('Document data: ${data}');
          setState(() {
            _counter = data['value'];
          });
        } else {
          print('The document does not exist on the database');
        }
      });
  }
```

(The _doc_ name will be different in your case!)

What does the code above?

- Gets the a specific document in the _Counter_ collection of your Firebase instance...
- If it succeeds, it calls a function that takes the data out of the document and sets the value to the counter.

On the other side, we want the `+` button to increment the value in Firebase.  
We need to _improve_ `_incrementCounter()`:

```dart
void _incrementCounter() {
  FirebaseFirestore.instance
    .collection('Counter')
    .doc('Qat49RJvyUkyWB48GWcK')
    .set({
      'value': _counter + 1,
    })
  .then((value) {
      setState(() {
        _counter++;
      });
      print("Counter incremented");
    })
    .catchError((error) => print("Failed to add to the counter: $error"));
}

```

[Here](01-syncronous/main.dart) you can get the complete [`main.dart`](01-syncronous/main.dart).

### Streams and having multiple users updating the same value

If you halready did the asynchronous Counter, you should probably startagain from a _clean_ `main.dart`.

The initialisation is the same as for the asynchronous example. Add the Firestore packages...

```dart
import 'package:firebase_core/firebase_core.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
```

... and make the `main()` function asyncronous for initializinging Firebase:

```dart
void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}
```

With a stream, we don't need to do any special initialization of the counter: the stream will be in charge of providing the current value.

First add to `_MyHomPageState`' a variable with the collection:

```dart
class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  CollectionReference _collection = FirebaseFirestore.instance.collection('Counter');

  ...
```

Then, modify `_MyHomPageState`'s `build` to use the stream:

```dart
body: StreamBuilder<QuerySnapshot>(
  stream: repository.getStream(),
  builder: (BuildContext context, snapshot) => Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Text(
            'You have pushed the button this many times:',
          ),
          Text(
            '$_counter',
            style: Theme.of(context).textTheme.headline4,
          ),
        ],
      ),
    ),
),
```

Instead of _simply_ creating a body, we're defining the `stream` to be used and add a function as the `builder` of the UI.

We're not showing the value from the stream yet.

Before doing that, we should convert the builder into a _real_ function (from an _arrow_ function) so that we can put multiple lines insde:

```dart
body: StreamBuilder<QuerySnapshot>(
  stream: _collection.snapshots(),
  builder: (BuildContext context, snapshot) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          Text(
            'You have pushed the button this many times:',
          ),
          Text(
            '$_counter',
            style: Theme.of(context).textTheme.headline4,
          ),
        ],
      ),
    );
  },
),
```

This allows to first update the counter from Firestore and then update the UI:

```dart
body: StreamBuilder<QuerySnapshot>(
  stream: _collection.snapshots(),
  builder: (BuildContext context, snapshot) {
    _counter = snapshot.data.docs[0].data()['value'];

    return Center(
            ...
            Text(
                '$_counter',
            ...
    );},
),
```

We could directly set the text as

```dart
Text(
  '${snapshot.data.docs[0].data()['value']},
```

But, then, we would have harder time implementing `_incrementCounter()` and we might have errors if the UI is built faster than the connection to Firestore.

As next, let's check that the value is ready and can be rendered:

```dart
builder: (BuildContext context, snapshot) {
  if (snapshot.hasError) {
    return Text('Something went wrong');
  }

  if (snapshot.connectionState == ConnectionState.waiting) {
    return Text("Loading");
  }
  
  if (snapshot.data.docs.isEmpty) {
    return Text("Document not found");
  }

  _counter = snapshot.data.docs[0].data()['value'];

  return Center(
    child: Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        Text(
          'You have pushed the button this many times:',
        ),
        Text(
          '$_counter',
          style: Theme.of(context).textTheme.headline4,
        ),
      ],
    ),
  );},
```

Finally, we need to get the value in Firestore to be incremented by writing the new value to the Firestore instance (instead of simply incrementing the `_counter` variable:

```dart
void _incrementCounter() {
  FirebaseFirestore.instance
    .collection('Counter')
    .doc('Qat49RJvyUkyWB48GWcK')
    .set({
      'value': _counter + 1,
    })
  .then((value) {
      print("Counter incremented");
    })
    .catchError((error) => print("Failed to add to the counter: $error"));
}
```

The biggest difference with the previous asyncronous example is that now we don't increment the `_counter` but let the stream to be updated and force the relevant part of the UI to be rendered.


[Here](02-reference/main.dart) you can get the complete [`main.dart`](02-reference/main.dart).

### Using a model

- "Creating the model classes" in [Firebase Tutorial for Flutter: Getting Started](https://www.raywenderlich.com/7426050-firebase-tutorial-for-flutter-getting-started).

## Good tutorials

- https://medium.com/firebase-tips-tricks/how-to-use-firebase-realtime-database-with-flutter-ebd98aba2c91

## Sources

- How to include and initialize (it's for firebase instead of firestore... but it's similar enough): [How to use Firebase realtime database with Flutter](https://medium.com/firebase-tips-tricks/how-to-use-firebase-realtime-database-with-flutter-ebd98aba2c91)
- [Cloud Firestore > Realtime changes](https://firebase.flutter.dev/docs/firestore/usage/#realtime-changes)
- [Firebase Tutorial for Flutter: Getting Started](https://www.raywenderlich.com/7426050-firebase-tutorial-for-flutter-getting-started).
  - Creating a DataRepository Class
  - Using Streams (without the model)

- https://firebase.google.com/docs/flutter/setup?platform=android
- https://www.raywenderlich.com/7426050
- https://firebase.flutter.dev/docs/firestore/usage/#read-data


## Further information

- [Firebase, a realtime database](https://medium.com/firebase-tips-tricks/how-to-use-firebase-realtime-database-with-flutter-ebd98aba2c91)

Have a look at https://codemagic.io/pricing/ for building iOS through CI

- https://blog.codemagic.io/native-android-getting-started-guide-with-codemagic-cicd/ 


Have a look at using Docker:

- https://medium.com/flutter-community/how-to-dockerize-flutter-apps-f2e54d6ec43c
