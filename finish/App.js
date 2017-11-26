import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import MapView from 'react-native-maps';
import { Button, Icon  } from 'react-native-elements';

export default class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            lat: 52.5027603,
            long: 13.4121008,
            towers: [],
        };
    }

    ortung() {
        sendingData(cellid, ss, this.state.lat, this.state.long)
    }

    render() {
        //var resending = scope.setInterval(sendingData, 60000);

        return (
            <View style = {
                styles.container} >
                <Text style={styles.heading}>OpenTowers</Text>
                <MapView style = {styles.map}
                         initialRegion={{
                    latitude: 52.5027603,
                    longitude: 13.4121008,
                    latitudeDelta: 0.0922,
                    longitudeDelta: 0.0421}}/>
                    <Icon
                    name="gps-fixed"
                    color={"#000000"}
                    onPress={() => this.ortung()}
                    //style={{height: 50, width: 50, textAlign: "flex-end"}}
                    />
            </View >
        );
    }
}

  const styles = StyleSheet.create({
      container: {
          backgroundColor: '#fff',
      },
      heading: {
          fontSize: 30,
          textAlign: 'center',
          backgroundColor: '#4286f4',
          width: '100%',
          height: 80,
          padding: 20,
          color: 'white',
          paddingLeft: 5,
      },
      map: {
          width: '100%',
          height:'80%',
      }
  });

function getData(lat, long){
    gps = lat + ' ' + long;
    get =  fetch('http://10.23.40.188:5000/api/get_message'), {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'gps': gps,
            }
        };
    get = get.json();
    this.setState({towers: get.placeholder})
}

function sendingData(cellid, ss, lat, long){
    //sending data to backend
    fetch('http://10.23.40.188:5000/api/post_message', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
                cellid: cellid,
                dataArray: {
                    signal_strength: ss,
                    location: {
                        long: long,
                        lat: lat
                    }
                }
            }
        )
    });
}