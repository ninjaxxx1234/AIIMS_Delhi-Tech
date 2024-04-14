import { View, Text, SafeAreaView, Image, TouchableOpacity, ScrollView } from 'react-native'
import { LinearGradient } from 'expo-linear-gradient';
import { Card } from '../components/'
import React, { useEffect, useState, useRef } from 'react'
import {
  LineChart,
  BarChart,
  PieChart,
  ProgressChart,
  ContributionGraph,
  StackedBarChart
} from "react-native-chart-kit";




const Fi02_DATA = {
  labels: ["0", "2", "4", "6", "May", "June", "July", "August", "September"],
  datasets: [
    {
      data: [
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100
      ]
    }
  ]
};
const PIP_DATA = {
  labels: ["0", "2", "4", "6", "May", "June", "July", "August", "September"],
  datasets: [
    {
      data: [
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100
      ]
    }
  ]
};
const VTe_DATA = {
  labels: ["0", "2", "4", "6", "May", "June", "July", "August", "September"],
  datasets: [
    {
      data: [
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100
      ]
    }
  ]
};
const RR_DATA = {
  labels: ["0", "2", "4", "6", "May", "June", "July", "August", "September"],
  datasets: [
    {
      data: [
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100
      ]
    }
  ]
};
const Tinsp_DATA = {
  labels: ["0", "2", "4", "6", "May", "June", "July", "August", "September"],
  datasets: [
    {
      data: [
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100
      ]
    }
  ]
};
const PEEP_DATA = {
  labels: ["0", "2", "4", "6", "May", "June", "July", "August", "September"],
  datasets: [
    {
      data: [
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100
      ]
    }
  ]
};
const HR_DATA = {
  labels: ["0", "2", "4", "6", "May", "June", "July", "August", "September"],
  datasets: [
    {
      data: [
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100
      ]
    }
  ]
};

const SP_DATA = {
  labels: ["0", "2", "4", "6", "May", "June", "July", "August", "September"],
  datasets: [
    {
      data: [
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100,
        Math.random() * 100
      ]
    }
  ]
};

let sample_timestamp = ["0", "2", "4", "6", "8", "10", "12", "14", "16"]
let sample_graphdata = [
  Math.random() * 100,
  Math.random() * 100,
  Math.random() * 100,
  Math.random() * 100,
  Math.random() * 100,
  Math.random() * 100,
  Math.random() * 100,
  Math.random() * 100,
  Math.random() * 100
]
const filePath = "../components/sample_data.txt";


const Home = () => {
  const intervalRef = useRef(null);
  const [graphData, setGraphData] = useState(sample_graphdata);
  const [timestamp, setTimestamp] = useState(sample_timestamp);
  const [graphName, setGraphName] = useState("Overall Wellbeing")
  const [SAMPLE_DATA, setSAMPLE_DATA] = useState(null);
  const [rrData, setRRData] = useState("22");
  const [vTeData, setvTeData] = useState("102");
  const [pipData, setPIPData] = useState("10");
  const [peepData, setPEEPData] = useState("10");
  const [fio2Data, setFIO2Data] = useState("30");
  const [spData, setspData] = useState("12");
  const [data, setData] = useState(HR_DATA)
  const [spArr, setSPArr] = useState(sample_graphdata);
  const [rrArr, setRRArr] = useState(sample_graphdata);
  const [fio2Arr, setFIO2Arr] = useState(sample_graphdata);
  const [pipArr, setPIPArr] = useState(sample_graphdata);
  const [peepArr, setPEEPArr] = useState(sample_graphdata);
  const [vteArr, setVTEArr] = useState(sample_graphdata);
  const [timeArr, setTimeArr] = useState(sample_graphdata);  

  const fetchJSON = () => {
    fetch("http://10.206.2.39:5000/data")
      .then(response => response.json())
      .then(data => {
        const { RR, Vte, PIP, PEEP, FiO2, SP, timestamp } = data;
        setSPArr(SP);
        setRRArr(RR);
        setFIO2Arr(FiO2);
        setVTEArr(Vte);
        setTimeArr(timestamp);
        setPEEPArr(PEEP);
        setPIPArr(PIP);
        if (data.RR && data.RR.length > 0) {
          setRRData(data.RR[data.RR.length - 1].toString());
          
        }
        if (data.Vte && data.Vte.length > 0) {
          setvTeData(data.Vte[data.Vte.length - 1].toString());
        }
        if (data.PIP && data.PIP.length > 0) {
          setPIPData(data.PIP[data.PIP.length - 1].toString());
        }
        if (data.PEEP && data.PEEP.length > 0) {
          setPEEPData(data.PEEP[data.PEEP.length - 1].toString());
        }
        if (data.FIO2 && data.FIO2.length > 0) {
          setFIO2Data(data.FIO2[data.FIO2.length - 1].toString());
        }
        if (data.SP && data.SP.length > 0) {
          setspData(data.SP[data.SP.length - 1].toString());
        }
      })
      .catch(error => {
        console.log('Error fetching data:', error)
      });
    }  
  
  

  const handleCardPress = (title) => {

    if (title === 'SP') {
      if (timeArr) {
        setGraphData(spArr);
        setTimestamp(timeArr)
      } else {
        setGraphData(sample_graphdata)
        setTimestamp(sample_timestamp)
      }
      setGraphName(title)
    } else if (title === 'FiO2') {
      if (timeArr) {
        setGraphData(fio2Arr);
        setTimestamp(timeArr)
      } else {
        setGraphData(sample_graphdata)
        setTimestamp(sample_timestamp)
      }
      setGraphName(title)
    } else if (title === 'PIP') {
      if (timeArr) {
        setGraphData(pipArr);
        setTimestamp(timeArr)
      } else {
        setGraphData(sample_graphdata)
        setTimestamp(sample_timestamp)
      }
      setGraphName(title)
    } else if (title === 'VTe') {
      if (timeArr) {
        setGraphData(vteArr);
        setTimestamp(timeArr)
      } else {
        setGraphData(sample_graphdata)
        setTimestamp(sample_timestamp)
      }
      setGraphName(title)
    } else if (title === 'RR') {
      if (timeArr) {
        setGraphData(rrArr);
        setTimestamp(timeArr)
      } else {
        setGraphData(sample_graphdata)
        setTimestamp(sample_timestamp)
      }
      setGraphName(title)
    } else if (title === 'Tinsp') {
      setGraphData(sample_graphdata);
      setTimestamp(sample_timestamp);
      setGraphName(title);
    } else if (title === 'PEEP') {
      if (timeArr) {
        setGraphData(peepArr);
        setTimestamp(timeArr)
      } else {
        setGraphData(sample_graphdata)
        setTimestamp(sample_timestamp)
      }
      setGraphName(title)
    } else if (title === 'HR') {
      setGraphData(sample_graphdata);
      setTimestamp(sample_timestamp);
      setGraphName(title);
    }


  };
  
  // Call fetchData initially
  
  useEffect(() => {
    fetchJSON();
    const interval = setInterval(fetchJSON, 3000);
    return () => {
      clearInterval(interval);
    };
  }, []); 
  
  
  return (

    <View className="w-full h-full flex-row bg-red-400">

      <View className=" relative flex-col items-center justify-center px-7 bg-white w-1/12">
        <View className=" absolute top-0 pt-14">
          <Image
            className="w-11 h-12"
            source={require('../assets/image 1.png')}
          />
        </View>
        <View className="items-center justify-center px-3 py-3 bg-blue-900 rounded-lg">
          <Image
            className="w-4 h-4"
            source={require('../assets/Vector1.png')}
          />
        </View>
        <View className="items-center justify-center px-3 py-5 bg-white rounded-lg">
          <Image
            className="w-4 h-4"
            source={require('../assets/Vector.png')}
          />
        </View>
        <View className="items-center justify-center px-3 py-5 bg-white rounded-lg">
          <Image
            className="w-4 h-4"
            source={require('../assets/Vector2.png')}
          />
        </View>
        <View className="items-center justify-center px-3 py-5 bg-white rounded-lg">
          <Image
            className="w-4 h-4"
            source={require('../assets/Vector3.png')}
          />
        </View>
        <View className="items-center justify-center px-3 py-5 bg-white rounded-lg">
          <Image
            className="w-4 h-4"
            source={require('../assets/Vector4.png')}
          />
        </View>
      </View>
      {/* Body of the Home Page*/}
      <LinearGradient

        className="w-full flex-row flex"
        colors={['#3F72AF', '#90ACCD']}
        start={{ x: 0, y: 0 }} // Left
        end={{ x: 1, y: 0 }}
      >
        <View className="flex-col w-2/3 z-10">

          <View className="flex-row justify-between pl-4 pt-12">

            <View >
              <Text className="text-3xl font-semibold text-white">Health Overview</Text>
            </View>

            <View className="ml-100  pr-12">
              <View className="flex-row space-x-4">
                <View className="bg-white rounded-lg h-11 w-11 items-center justify-center">
                  <Image
                    className="w-7 h-7"
                    source={require('../assets/frame2.png')}
                  />
                </View>
                <View className="bg-white rounded-lg h-11 w-11 items-center justify-center">
                  <Image
                    className="w-7 h-7"
                    source={require('../assets/frame3.png')}
                  />
                </View>
              </View>
            </View>
          </View>




          <View className="flex-row">
            <View className="pl-4 ">
              <Text className="text-m text-white font-light">April, 15 2024</Text>
            </View>
          </View>

          <View>
            <View className="flex-row pt-3">
              <View className="flex-1 flex-row justify-around space-x-7">
                <Card
                  imageUri={require('../assets/Group 14.png')}
                  iconBgColor="bg-orange-200"
                  textBgColor="bg-orange-200"
                  title="FiO2"
                  value={fio2Data}
                  units="%"
                  remark="Normal"
                  onPress={handleCardPress}
                />
                <Card
                  imageUri={require('../assets/pip-icon.png')}
                  iconBgColor="bg-rose-200"
                  textBgColor="bg-rose-200"
                  title="PIP"
                  value={pipData}
                  units="cmH20"
                  remark="Normal"
                  onPress={handleCardPress}
                />
                <Card
                  imageUri={require('../assets/vte-icon.png')}
                  iconBgColor="bg-cyan-200"
                  textBgColor="bg-cyan-200"
                  title="VTe"
                  value={vTeData}
                  units="mL"
                  remark="Normal"
                  onPress={handleCardPress}
                />
                <Card
                  imageUri={require('../assets/rr-icon.png')}
                  iconBgColor="bg-purple-200"
                  textBgColor="bg-purple-200"
                  title="RR"
                  value={rrData}
                  units="bpm"
                  remark="Normal"
                  onPress={handleCardPress}
                />
              </View>
            </View>
          </View>
          <View>
            <View className="flex-row pt-3">
              <View className="flex-1 flex-row justify-around space-x-7">
                <Card
                  imageUri={require('../assets/sp-icon2.png')}
                  iconBgColor="bg-emerald-100"
                  textBgColor="bg-emerald-100"
                  title="SP"
                  value={spData}
                  units="cmH2O"
                  remark="Normal"
                  onPress={handleCardPress}
                />
                <Card
                  imageUri={require('../assets/tinsp-icon.png')}
                  iconBgColor="bg-yellow-100"
                  textBgColor="bg-yellow-100"
                  title="Tinsp"
                  value="123"
                  units="mmHg"
                  remark="Normal"
                  onPress={handleCardPress}
                />
                <Card
                  imageUri={require('../assets/peep-icon2.png')}
                  iconBgColor="bg-rose-200"
                  textBgColor="bg-rose-200"
                  title="PEEP"
                  value={peepData}
                  units="cmH20"
                  remark="Normal"
                  onPress={handleCardPress}
                />
                <Card
                  imageUri={require('../assets/hr-icon.png')}
                  iconBgColor="bg-sky-200"
                  textBgColor="bg-sky-200"
                  title="HR"
                  value="78"
                  units="bpm"
                  remark="Normal"
                  onPress={handleCardPress}
                />
              </View>
            </View>
            <View className="">
              <View className=" items-center p-4">
                <View className="h-72 w-full bg-white rounded-xl">
                  <View className="flex-row justify-between w-full ">
                    <Text className=" pl-4 pt-2 pb-5 text-2xl font-medium">{graphName}</Text>
                    <View className="pr-6 p-4 pt-3">
                      <TouchableOpacity className="pr-4 border-2 border-gray-300 w-20 h-8 items-center justify-between flex-row rounded-lg">
                        <Text className="pl-2 text-sm">3hrs</Text>
                        <Image
                          className="h-4 w-4 pt-2"
                          source={require('../assets/downarrow-icon.png')}
                        />
                      </TouchableOpacity>
                    </View>
                  </View>

                  <LineChart
                    // data={{
                    //   labels: ["0", "2", "4", "6", "May", "June", "July", "August", "September"],
                    //   datasets: [
                    //     {
                    //       data: [Math.random()*100, Math.random()*100, Math.random()*100, Math.random()*100, Math.random()*100, Math.random()*100, Math.random()*100, Math.random()*100, Math.random()*100,]
                    //     }
                    //   ]
                    // }}
                    data={{
                      labels: timeArr,
                      datasets: [
                        {
                          data: graphData
                        }
                      ]
                    }}
                    width={830}
                    height={220}
                    
                    yAxisSuffix="mL"
                    yAxisInterval={1}
                    chartConfig={{
                      backgroundColor: "#FFFFFF", // Change background color to white
                      backgroundGradientFrom: "#FFFFFF",
                      backgroundGradientTo: "#FFFFFF",
                      decimalPlaces: 2,
                      color: (opacity = 1) => `rgba(243, 165, 63, ${opacity})`, // Orange color
                      labelColor: (opacity = 1) => `rgba(0, 0, 0, ${opacity})`,
                      style: {
                        borderRadius: 16
                      },
                      gradient: true, // Apply gradient to the area under the graph
                      fillShadowGradient: "#FDFFA7" // Set the fill shadow gradient color
                    }}
                    bezier
                    style={{
                      marginVertical: 8,
                      paddingLeft: 22,
                      borderRadius: 16
                    }}
                  />

                </View>



              </View>
            </View>
          </View>
        </View>

        <LinearGradient

          className="flex-col w-1/4 rounded-xl"
          colors={['#10527E', '#052F4B']}
          start={{ x: 0, y: 0 }} // Left
          end={{ x: 1, y: 0 }}
        >
          <View className="py-6 items-center justify-between px-4 flex-row ">
            <Text className="text-xl font-semibold text-white">Patient Details</Text>

            <TouchableOpacity className="flex-row border border-white w-16 h-8 rounded-lg items-center justify-center">
              <Text className="text-gray-100">Bed 3</Text>
              <Image
                className="pl-2 w-4 h-4"
                source={require('../assets/downarrow-icon.png')}
              />
            </TouchableOpacity>
          </View>


          <View className="justify-center items-center w-80 flex flex-row h-12">
            <View className="w-2 h-4 bg-red-500"></View>
            <View className="px-1 bg-white h-8 w-72 justify-start items-center rounded-lg flex-row">
              <Text className="pl-2 text-gray-300">Name:</Text>
              <Text className="pl-10">Vijay Kumar IPS</Text>
            </View>
          </View>
          <View className="justify-start gap-x-6 w-full px-3 items-start mt-1 flex flex-row">
            <View className="flex flex-col gap-y-3">
              <View className="flex-row items-center">
                <View className="w-2 h-4 bg-red-500"></View>
                <View className="bg-white w-28 h-8 justify-start items-center rounded-lg flex-row">
                  <Text className="pl-2 text-gray-300">Age:</Text>
                  <Text className="pl-4">54</Text>
                </View>
              </View>

              <View className="flex-row items-center">
                <View className="w-2 h-4 bg-red-500"></View>
                <View className="bg-white w-28 h-8 justify-start items-center rounded-lg flex-row">
                  <Text className="pl-2 text-gray-300">Age:</Text>
                  <Text className="pl-4">54</Text>
                </View>
              </View>

              <View className="flex-row items-center">
                <View className="w-2 h-4 bg-red-500"></View>
                <View className="bg-white w-28 h-8 justify-start items-center rounded-lg flex-row">
                  <Text className="pl-2 text-gray-300">Age:</Text>
                  <Text className="pl-4">54</Text>
                </View>
              </View>

              <View className="flex-row items-center">
                <View className="w-2 h-4 bg-red-500"></View>
                <View className="bg-white w-28 h-8 justify-start items-center rounded-lg flex-row">
                  <Text className="pl-2 text-gray-300">Age:</Text>
                  <Text className="pl-4">54</Text>
                </View>
              </View>

              <View className="flex-row items-center">
                <View className="w-2 h-4 bg-red-500"></View>
                <View className="bg-white w-28 h-8 justify-start items-center rounded-lg flex-row">
                  <Text className="pl-2 text-gray-300">Age:</Text>
                  <Text className="pl-4">54</Text>
                </View>
              </View>

            </View>

            <View className="flex flex-col gap-y-3">
              <View className="flex flex-row items-center">
                <View className="w-2 h-4 bg-red-500"></View>
                <View className="bg-white w-36 h-8 justify-start items-center rounded-lg flex-row">
                  <Text className="pl-2 text-gray-300">Blood Group:</Text>
                  <Text className="pl-3 text-xs">A+</Text>
                </View>
              </View>
              <View className="flex flex-row items-center">
                <View className="w-2 h-4 bg-red-500"></View>
                <View className="bg-white w-36 h-8 justify-start items-center rounded-lg flex-row">
                  <Text className="pl-2 text-gray-300">Blood Group:</Text>
                  <Text className="pl-3 text-xs">A+</Text>
                </View>
              </View>
              <View className="flex flex-row items-center pt-1">
                <View className="w-2 h-8 bg-red-500"></View>
                <View className="bg-[#F8DEBD] px-4 w-36 justify-start items-center rounded-lg flex-col gap-y-1 flex">
                  <Image
                    className="w-full object-contain scale-x-[-1]"
                    source={require('../assets/dashboard/Scale.png')}
                  />
                  <View className="flex-row justify-around w-full mb-1">
                      <Text>Height:</Text>
                      <Text>183cm</Text>
                  </View>
                </View>
              </View>
              <View className="flex flex-row items-center pt-1">
                <View className="w-2 h-8 bg-red-500"></View>
                <View className="bg-[#D0FBFF] px-4 w-36 justify-start items-center rounded-lg flex-col gap-y-1 flex">
                  <Image
                    className="w-full object-contain scale-x-[-1]"
                    source={require('../assets/dashboard/Scale.png')}
                  />
                  <View className="flex-row justify-around w-full mb-1">
                      <Text>Weight:</Text>
                      <Text>72kg</Text>
                  </View>
                </View>
              </View>
            </View>


          </View>




          <View className="py-6 items-center justify-between px-4 flex-row ">
            <Text className="text-xl font-semibold text-white">Last Checked</Text>

            <TouchableOpacity className="flex-row border border-white w-16 h-8 rounded-lg items-center justify-center">
              <Text className="text-gray-100">1hr</Text>
              <Image
                className="pl-2 w-4 h-4"
                source={require('../assets/downarrow-icon.png')}
              />
            </TouchableOpacity>
          </View>
          <ScrollView>
            <View className="justify-center items-center  h-20">
              <View className="px-1 bg-white w-80 h-14 justify-around items-center rounded-lg flex-row">
                <View className="bg-blue-300 h-8 w-20 rounded-lg items-center justify-center">
                  <Text className="text-black text-xs">14/04/2024</Text>
                </View>
                <View className="bg-blue-950 h-8 w-20 rounded-lg items-center justify-center">
                  <Text className="text-white text-xs">14/04/2024</Text>
                </View>
                <View className="bg-sky-200 h-8 w-20 rounded-lg items-center justify-center">
                  <Text className="text-black text-m">RN Richie</Text>
                </View>
              </View>
            </View>
            <View className="justify-center items-center  h-20">
              <View className="px-1 bg-white w-80 h-14 justify-around items-center rounded-lg flex-row">
                <View className="bg-blue-300 h-8 w-20 rounded-lg items-center justify-center">
                  <Text className="text-black text-xs">14/04/2024</Text>
                </View>
                <View className="bg-blue-950 h-8 w-20 rounded-lg items-center justify-center">
                  <Text className="text-white text-xs">14/04/2024</Text>
                </View>
                <View className="bg-sky-200 h-8 w-20 rounded-lg items-center justify-center">
                  <Text className="text-black text-m">RN Richie</Text>
                </View>
              </View>
            </View>
            <View className="justify-center items-center  h-20">
              <View className="px-1 bg-white w-80 h-14 justify-around items-center rounded-lg flex-row">
                <View className="bg-blue-300 h-8 w-20 rounded-lg items-center justify-center">
                  <Text className="text-black text-xs">14/04/2024</Text>
                </View>
                <View className="bg-blue-950 h-8 w-20 rounded-lg items-center justify-center">
                  <Text className="text-white text-xs">14/04/2024</Text>
                </View>
                <View className="bg-sky-200 h-8 w-20 rounded-lg items-center justify-center">
                  <Text className="text-black text-m">RN Richie</Text>
                </View>
              </View>
            </View>
            <View className="justify-center items-center  h-20">
              <View className="px-1 bg-white w-80 h-14 justify-around items-center rounded-lg flex-row">
                <View className="bg-blue-300 h-8 w-20 rounded-lg items-center justify-center">
                  <Text className="text-black text-xs">14/04/2024</Text>
                </View>
                <View className="bg-blue-950 h-8 w-20 rounded-lg items-center justify-center">
                  <Text className="text-white text-xs">14/04/2024</Text>
                </View>
                <View className="bg-sky-200 h-8 w-20 rounded-lg items-center justify-center">
                  <Text className="text-black text-m">RN Richie</Text>
                </View>
              </View>
            </View>
            <View className="justify-center items-center  h-20">
              <View className="px-1 bg-white w-80 h-14 justify-around items-center rounded-lg flex-row">
                <View className="bg-blue-300 h-8 w-20 rounded-lg items-center justify-center">
                  <Text className="text-black text-xs">14/04/2024</Text>
                </View>
                <View className="bg-blue-950 h-8 w-20 rounded-lg items-center justify-center">
                  <Text className="text-white text-xs">14/04/2024</Text>
                </View>
                <View className="bg-sky-200 h-8 w-20 rounded-lg items-center justify-center">
                  <Text className="text-black text-m">RN Richie</Text>
                </View>
              </View>
            </View>
            <View className="justify-center items-center  h-20">
              <View className="px-1 bg-white w-80 h-14 justify-around items-center rounded-lg flex-row">
                <View className="bg-blue-300 h-8 w-20 rounded-lg items-center justify-center">
                  <Text className="text-black text-xs">14/04/2024</Text>
                </View>
                <View className="bg-blue-950 h-8 w-20 rounded-lg items-center justify-center">
                  <Text className="text-white text-xs">14/04/2024</Text>
                </View>
                <View className="bg-sky-200 h-8 w-20 rounded-lg items-center justify-center">
                  <Text className="text-black text-m">RN Richie</Text>
                </View>
              </View>
            </View>
          </ScrollView>
        </LinearGradient>

      </LinearGradient>


    </View>

  )
}

export default Home