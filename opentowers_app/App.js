import React from 'react';
import {
    StyleSheet,
    Text,
    View
} from 'react-native';
import MapView from 'react-native-maps';
import { Button } from 'react-native-elements';

export default class App extends React.Component {
    render() {
        return ( <View style = {
                styles.container} >
                <Text style={styles.heading}>OpenTowers</Text>
                <MapView style = {
                styles.map} initialRegion={{
                    latitude: 52.5027603,
                    longitude: 13.4121008,
                    latitudeDelta: 0.0922,
                    longitudeDelta: 0.0421,
                   }}
               />
               <Button
                raised
                icon={{name: 'cached'}}
                title='Daten auffangen...' />
                </View>
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
        fontFamily: 'sans-serif',
    },
    map: {
      width: '100%',
      height:'80%',
    }
});
