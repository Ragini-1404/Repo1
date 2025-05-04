public class LinearSearchExample {
    
    // Method to perform linear search
    public static Integer linearSearch(List<Integer> numbers, Integer target) {
        for (Integer i = 0; i < numbers.size(); i++) {
            if (numbers[i] == target) {
                return i; // Return the index if found
            }
        }
        return -1; // Return -1 if not found
    }
    
    // Test method to demonstrate the search
    public static void runSearch() {
        List<Integer> myList = new List<Integer>{10, 20, 30, 40, 50};
        Integer searchValue = 30;
        
        Integer resultIndex = linearSearch(myList, searchValue);
        
        if (resultIndex != -1) {
            System.debug('Value ' + searchValue + ' found at index: ' + resultIndex);
        } else {
            System.debug('Value ' + searchValue + ' not found.');
        }
    }
}
