
import { SafeAreaView, StyleSheet, Text, View } from 'react-native';
import { Home, Settings, Profile, Exit, Overall } from "./screens";

import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { NavigationContainer } from '@react-navigation/native';


const Tab = createBottomTabNavigator();



export default function App() {
  return (
    <Home />
  );
}


