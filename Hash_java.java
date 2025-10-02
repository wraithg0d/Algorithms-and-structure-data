// Добавить значение
map.put("key", value);

// Получить значение  
Integer value = map.get("key");

// Проверить наличие
boolean exists = map.containsKey("key");

// Удалить ключ
map.remove("key");

// Узнать размер
int size = map.size();

// Вывести все элементы
for (Map.Entry<String, Integer> entry : map.entrySet()) {
    System.out.println(entry.getKey() + ": " + entry.getValue());
}
