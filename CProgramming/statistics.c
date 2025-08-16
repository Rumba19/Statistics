#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function to calculate mean
double calculate_mean(int arr[], int n) {
    if (n == 0) return 0.0;
    
    long sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return (double)sum / n;
}

// Comparison function for qsort
int compare(const void *a, const void *b) {
    return (*(int*)a - *(int*)b);
}

// Function to calculate median
double calculate_median(int arr[], int n) {
    if (n == 0) return 0.0;
    
    // Create a copy for sorting to preserve original array
    int *sorted = malloc(n * sizeof(int));
    memcpy(sorted, arr, n * sizeof(int));
    
    qsort(sorted, n, sizeof(int), compare);
    
    double median;
    if (n % 2 == 0) {
        median = (sorted[n/2 - 1] + sorted[n/2]) / 2.0;
    } else {
        median = sorted[n/2];
    }
    
    free(sorted);
    return median;
}

// Structure to hold mode results
typedef struct {
    int *modes;
    int count;
    int max_frequency;
} ModeResult;

// Function to calculate mode
ModeResult calculate_mode(int arr[], int n) {
    ModeResult result = {NULL, 0, 0};
    
    if (n == 0) return result;
    
    // Find unique values and their frequencies
    int *unique_values = malloc(n * sizeof(int));
    int *frequencies = malloc(n * sizeof(int));
    int unique_count = 0;
    
    for (int i = 0; i < n; i++) {
        int found = 0;
        for (int j = 0; j < unique_count; j++) {
            if (unique_values[j] == arr[i]) {
                frequencies[j]++;
                found = 1;
                break;
            }
        }
        if (!found) {
            unique_values[unique_count] = arr[i];
            frequencies[unique_count] = 1;
            unique_count++;
        }
    }
    
    // Find maximum frequency
    int max_freq = 0;
    for (int i = 0; i < unique_count; i++) {
        if (frequencies[i] > max_freq) {
            max_freq = frequencies[i];
        }
    }
    
    // Count how many values have maximum frequency
    int mode_count = 0;
    for (int i = 0; i < unique_count; i++) {
        if (frequencies[i] == max_freq) {
            mode_count++;
        }
    }
    
    // Collect all mode values
    result.modes = malloc(mode_count * sizeof(int));
    result.count = mode_count;
    result.max_frequency = max_freq;
    
    int mode_index = 0;
    for (int i = 0; i < unique_count; i++) {
        if (frequencies[i] == max_freq) {
            result.modes[mode_index++] = unique_values[i];
        }
    }
    
    free(unique_values);
    free(frequencies);
    return result;
}

// Function to print array
void print_array(int arr[], int n) {
    printf("[");
    for (int i = 0; i < n; i++) {
        printf("%d", arr[i]);
        if (i < n - 1) printf(", ");
    }
    printf("]");
}

// Function to free mode result
void free_mode_result(ModeResult *result) {
    if (result->modes) {
        free(result->modes);
        result->modes = NULL;
    }
}

int main() {
    // Test data
    int data1[] = {1, 2, 3, 4, 5};
    int data2[] = {1, 2, 2, 3, 4, 4, 4};
    int data3[] = {5, 5, 3, 3, 1, 1};
    int data4[] = {10};
    
    int *test_arrays[] = {data1, data2, data3, data4};
    int sizes[] = {5, 7, 6, 1};
    int num_tests = 4;
    
    printf("=== C Statistics Calculator (Procedural Approach) ===\n\n");
    
    for (int i = 0; i < num_tests; i++) {
        printf("Test %d: ", i + 1);
        print_array(test_arrays[i], sizes[i]);
        printf("\n");
        
        double mean = calculate_mean(test_arrays[i], sizes[i]);
        printf("Mean: %.2f\n", mean);
        
        double median = calculate_median(test_arrays[i], sizes[i]);
        printf("Median: %.2f\n", median);
        
        ModeResult mode_result = calculate_mode(test_arrays[i], sizes[i]);
        printf("Mode: ");
        for (int j = 0; j < mode_result.count; j++) {
            printf("%d", mode_result.modes[j]);
            if (j < mode_result.count - 1) printf(", ");
        }
        printf(" (frequency: %d)\n", mode_result.max_frequency);
        
        free_mode_result(&mode_result);
        printf("\n");
    }
    
    return 0;
}