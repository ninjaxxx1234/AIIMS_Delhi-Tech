import { View, Text, Image, TouchableOpacity } from 'react-native';
import React from 'react';

const Card = ({ imageUri, iconBgColor, textBgColor, title, value, units, remark, onPress }) => {
  return (
    <TouchableOpacity
      onPress={() => onPress(title)} 
      className="flex-col bg-white h-36 w-48 rounded-xl pl-6"
    >
      <View className="flex-row pt-5 gap-x-2">
        <View className={`${iconBgColor} h-12 w-12 items-center justify-center rounded-lg`}>
          <Image
            className="h-6 w-6"
            source={imageUri}
          />
        </View>
        <Text className=" pt-2 text-2xl font-medium text-black">{title}</Text>
      </View>
      <View className="flex-row gap-x-1 ml-1">
        <Text className="pt-2 text-3xl">{value}</Text>
        <Text className="pt-4 text-m text-gray-600">{units}</Text>
      </View>
      <View className="h-10 w-20">
        <View className={`mt-1 ${textBgColor} h-5 w-14 justify-center items-center rounded-md`}>
          <Text className="text-xs">{remark}</Text>
        </View>
      </View>
    </TouchableOpacity>
  );
};

export default Card;
