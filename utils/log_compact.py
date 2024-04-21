import os
import re



def process_log_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        non_zero_entries = [line.strip() for line in lines if 'new items: 0' not in line]
        if non_zero_entries:
            # Extract the date and time from the file name
            datetime_match = re.search(r'(\d{8})_(\d{2})(\d{2})(\d{2})', file_path)
            date = datetime_match.group(1) if datetime_match else "Unknown Date"
            time = datetime_match.group(2) + ':' + datetime_match.group(3) + ':' + datetime_match.group(4) if datetime_match else "Unknown Time"
            # Include date and time in the first line where the file name exists
            first_line = f"Date: {date[:4]}/{date[4:6]}/{date[6:]} {time}\n" if non_zero_entries[0].startswith("Country:") else ""
            return first_line + '\n'.join(non_zero_entries) + '\n' + '-' * 60 + '\n'
        else:
            return ''

def main():
    summary_file_path = "summary.txt"
    log_directory = "logs_old"

    with open(summary_file_path, 'w') as summary_file:
        for filename in os.listdir(log_directory):
            if filename.endswith(".log"):
                file_path = os.path.join(log_directory, filename)
                summary_entry = process_log_file(file_path)
                if summary_entry:
                    summary_file.write(summary_entry)

if __name__ == "__main__":
    main()