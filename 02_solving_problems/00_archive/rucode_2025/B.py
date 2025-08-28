def main():
    input_data = input().strip()
    
    if ':' in input_data:
        time_parts = input_data.split(':')
        hours = int(time_parts[0])
        minutes = int(time_parts[1])
        seconds = int(time_parts[2])
        
        total_seconds = hours * 3600 + minutes * 60 + seconds
        print(total_seconds)
    else:
        total_seconds = int(input_data)
        
        hours = total_seconds // 3600
        remaining_seconds = total_seconds % 3600
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

if __name__ == "__main__":
    main()
