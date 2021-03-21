import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class DataRepository {
  final CollectionReference collection = FirebaseFirestore.instance.collection('Counter');

  Stream<QuerySnapshot> getStream() {
    return collection.snapshots();
  }
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  CollectionReference _collection = FirebaseFirestore.instance.collection('Counter');

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


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: StreamBuilder<QuerySnapshot>(
        stream: _collection.snapshots(),
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
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: Icon(Icons.add),
      ),
    );
  }
}
