import subprocess as cmd
import platform
import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
import threading

def money_ape():
    print("\033[1;93m __  __                                _          \033[0m")
    print("\033[1;93m|  \\/  | ___  _ __   ___ _   _        / \\   _ __   ___ \033[0m")
    print("\033[1;93m| |\\/| |/ _ \\| '_ \\ / _ \\ | | |_____ / _ \\ | '_ \\ / _ \\\033[0m")
    print("\033[1;93m| |  | | (_) | | | |  __/ |_| |_____/ ___ \\| |_) |  __/\033[0m")
    print("\033[1;93m|_|  |_|\\___/|_| |_|\\___|\\__, |    /_/   \\_\\ .__/ \\___|\033[0m")
    print("\033[1;93m                         |___/             |_|\033[0m")
    print("\033[1;32m\n                    Github : Money-Ape\033[0m {verison : 1.0.0}\n")

money_ape()

current_os = platform.system()

def env_var_path():
    try:
        spath = r"ffmpeg"
        dpath = r"C:\\ffmpeg"
        cmd.run(["robocopy", spath, dpath, "/E", "/NFL", "/NDL", "/NJH", "/NJS", "/nc", "/ns", "/np"], check=True)
        cmd.run(["setx", "/M", "Path", f"%Path%;{dpath}\\bin" ], check=True)
        print("\033[1;32m[INFO] : ffmpeg installed successfully and path has been added to environment variable.!!")
    except cmd.CalledProcessError as e:
        print(f"\033[1;31m[ERROR]\033[0m: Command failed with exit code {e.returncode}\n")
        print("\033[1;31mThe Program should be executed with Administration.!\033[0m")
    except Exception as e:
        print(f"\033[1;33m[WARNING]\033[0m: {e}.!")

def OS_platform_verify():
    global current_os
    if current_os == "Windows":
        print(f"Platform Detected.! = {current_os}\n")
        module_names = ["yt_dlp", "tabulate", "tkinter"]
        for module_name in module_names:
            try:
                __import__(module_name)
                print(f"{module_name}.......ok")
                print(f"{module_name} is already installed.\n")
            except:
                print(f"{module_name}.......Error")
                print(f"{module_name} is not installed.\nInstalling...")
                try:
                    cmd.run(["cmd", "/c", "pip3", "install", module_name, "--quiet"])
                    print(f"{module_name} installed successfully.\n")
                except cmd.CalledProcessError:
                    print(f"Failed to install {module_name}.\n")
    elif current_os == "Linux":
        print(f"Platform Detected.! = {current_os}\n")
        module_names = ["yt_dlp", "tabulate", "tkinter"]
        for module_name in module_names:
            try:
                __import__(module_name)
                print(f"{module_name}.......ok")
                print(f"{module_name} is already installed.\n")
            except:
                print(f"{module_name}.......Error")
                print(f"{module_name} is not installed.\nInstalling...")
                try:
                    cmd.run(["cmd", "/c", "pip3", "install", module_name, "--quiet"])
                    print(f"{module_name} installed successfully.\n")
                except cmd.CalledProcessError:
                    print(f"Failed to install {module_name}.\n")
    else:
        print("This file isn't compatible on this system.!!")

env_var_path()
OS_platform_verify()

import yt_dlp
from tabulate import tabulate

def format_file_size(size):
    if size is None:
        return "Unknown"
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0

def video_formats(url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            formats = info.get('formats', [])

        formats_dict = {}
        for fmt in formats:
            format_id = fmt['format_id']
            filesize = fmt.get('filesize_approx', fmt.get('filesize'))
            formats_dict[format_id] = {
                'Resolution': fmt.get('resolution'),
                'Filesize': format_file_size(filesize)
            }
        return formats_dict, info.get('title', 'Unknown Title')
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

class Tubit:
    def __init__(self, root):
        self.root = root
        self.root.title("Money-Ape : Pytube")
        self.root.geometry("1400x900")
        self.root.configure(bg='#1a1a1a')
        self.root.resizable(True, True)
        
        # Configure style for modern look
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure colors - Much darker theme
        self.bg_color = '#0d1117'
        self.card_color = '#161b22'
        self.input_bg = '#21262d'
        self.accent_color = '#238636'
        self.text_color = '#f0f6fc'
        self.muted_text = '#8b949e'
        self.border_color = '#30363d'
        
        # Download progress variables
        self.video_title = ""
        self.download_progress = 0
        
        self.setup_ui()
        
    def setup_ui(self):
        # Main container with reduced padding
        main_container = tk.Frame(self.root, bg=self.bg_color)
        main_container.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # Header with reduced padding
        header_frame = tk.Frame(main_container, bg=self.bg_color)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Title
        title_frame = tk.Frame(header_frame, bg=self.bg_color)
        title_frame.pack()
        
        title_label = tk.Label(title_frame, text="Tubit", 
                             font=('Arial', 28, 'bold'), 
                             bg=self.bg_color, fg=self.text_color)
        title_label.pack(side=tk.LEFT)
        
        subtitle_label = tk.Label(header_frame, text="Download YouTube videos in your preferred quality", 
                                font=('Arial', 12), 
                                bg=self.bg_color, fg=self.muted_text)
        subtitle_label.pack(pady=(5, 0))
        
        # URL Input Section with reduced padding
        url_frame = tk.Frame(main_container, bg=self.card_color, relief=tk.FLAT, highlightbackground=self.border_color, highlightthickness=1)
        url_frame.pack(fill=tk.X, pady=(0, 15))
        
        url_inner = tk.Frame(url_frame, bg=self.card_color)
        url_inner.pack(fill=tk.X, padx=20, pady=20)
        
        url_label = tk.Label(url_inner, text="YouTube URL", 
                           font=('Arial', 12, 'bold'), 
                           bg=self.card_color, fg=self.text_color)
        url_label.pack(anchor=tk.W, pady=(0, 8))
        
        # Center the URL input
        url_input_frame = tk.Frame(url_inner, bg=self.card_color)
        url_input_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.url_entry = tk.Entry(url_input_frame, font=('Arial', 12), 
                                bg=self.input_bg, fg=self.text_color, 
                                insertbackground=self.text_color,
                                relief=tk.FLAT, bd=0, justify='center',
                                highlightbackground=self.border_color, highlightthickness=1)
        self.url_entry.pack(fill=tk.X, ipady=12)
        
        # Center the fetch button
        button_frame = tk.Frame(url_inner, bg=self.card_color)
        button_frame.pack()
        
        self.fetch_button = tk.Button(button_frame, text="Fetch Formats", 
                                    command=self.fetch_formats_threaded,
                                    bg=self.accent_color, fg='white', 
                                    font=('Arial', 12, 'bold'),
                                    relief=tk.FLAT, bd=0, cursor='hand2',
                                    activebackground='#2ea043', padx=25, pady=10)
        self.fetch_button.pack()
        
        # Two-column content area 
        content_frame = tk.Frame(main_container, bg=self.card_color, highlightbackground=self.border_color, highlightthickness=1)
        content_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        
        # Two-column layout
        two_col_frame = tk.Frame(content_frame, bg=self.card_color)
        two_col_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Left column - Examples & Guide
        left_frame = tk.Frame(two_col_frame, bg=self.card_color)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))
        
        left_header = tk.Label(left_frame, text="Examples & Guide", 
                             font=('Arial', 12, 'bold'), 
                             bg=self.card_color, fg=self.text_color)
        left_header.pack(anchor=tk.W, pady=(0, 8))
        
        self.formats_text = scrolledtext.ScrolledText(left_frame, wrap=tk.WORD, 
                                                    width=50, height=20,
                                                    bg='#0d1117', fg=self.text_color,
                                                    font=('Consolas', 10),
                                                    relief=tk.FLAT, bd=0,
                                                    insertbackground=self.text_color,
                                                    selectbackground=self.accent_color,
                                                    selectforeground='white')
        self.formats_text.pack(fill=tk.BOTH, expand=True)
        
        # Right column - Format Details
        right_frame = tk.Frame(two_col_frame, bg=self.card_color)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(10, 0))
        
        right_header = tk.Label(right_frame, text="Format Details", 
                              font=('Arial', 12, 'bold'), 
                              bg=self.card_color, fg=self.text_color)
        right_header.pack(anchor=tk.W, pady=(0, 8))
        
        self.text_area = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, 
                                                 width=50, height=20,
                                                 bg='#0d1117', fg=self.text_color,
                                                 font=('Consolas', 10),
                                                 relief=tk.FLAT, bd=0,
                                                 insertbackground=self.text_color,
                                                 selectbackground=self.accent_color,
                                                 selectforeground='white')
        self.text_area.pack(fill=tk.BOTH, expand=True)
        
        # Set initial example text
        self.set_initial_example_text()
        
        # Bottom section - FIXED LAYOUT: Video Title LEFT, Download Controls RIGHT
        bottom_frame = tk.Frame(main_container, bg=self.card_color, highlightbackground=self.border_color, highlightthickness=1)
        bottom_frame.pack(fill=tk.X)
        
        bottom_inner = tk.Frame(bottom_frame, bg=self.card_color)
        bottom_inner.pack(fill=tk.X, padx=20, pady=15)  # Reduced padding
        
        # HORIZONTAL LAYOUT: Video Title (LEFT) + Download Controls (RIGHT)
        main_bottom_frame = tk.Frame(bottom_inner, bg=self.card_color)
        main_bottom_frame.pack(fill=tk.X, pady=(0, 10))
        
        # LEFT SIDE - Video Title Section
        video_title_section = tk.Frame(main_bottom_frame, bg=self.card_color)
        video_title_section.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 20))
        
        video_title_label = tk.Label(video_title_section, text="Video Title:", 
                                   font=('Arial', 12, 'bold'), 
                                   bg=self.card_color, fg=self.text_color)
        video_title_label.pack(anchor=tk.W, pady=(0, 5))
        
        # Video title display with background
        video_title_container = tk.Frame(video_title_section, bg=self.input_bg, highlightbackground=self.border_color, highlightthickness=1)
        video_title_container.pack(fill=tk.X)
        
        self.video_title_display = tk.Label(video_title_container, text="No video selected", 
                                          font=('Arial', 11), 
                                          bg=self.input_bg, fg=self.muted_text,
                                          wraplength=600, justify=tk.LEFT, anchor='w')
        self.video_title_display.pack(fill=tk.X, padx=15, pady=10)
        
        # RIGHT SIDE - Download Controls
        download_controls_section = tk.Frame(main_bottom_frame, bg=self.card_color)
        download_controls_section.pack(side=tk.RIGHT)
        
        download_header = tk.Label(download_controls_section, text="Download Control", 
                                 font=('Arial', 12, 'bold'), 
                                 bg=self.card_color, fg=self.text_color)
        download_header.pack(anchor=tk.W, pady=(0, 5))
        
        # Download controls in a compact layout
        controls_container = tk.Frame(download_controls_section, bg=self.card_color)
        controls_container.pack()
        
        format_label = tk.Label(controls_container, text="Format Code:", 
                              font=('Arial', 10, 'bold'), 
                              bg=self.card_color, fg=self.text_color)
        format_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.format_entry = tk.Entry(controls_container, font=('Arial', 11), 
                                   bg=self.input_bg, fg=self.text_color,
                                   insertbackground=self.text_color,
                                   relief=tk.FLAT, bd=0, justify='center',
                                   highlightbackground=self.border_color, highlightthickness=1,
                                   width=15)
        self.format_entry.pack(ipady=8, pady=(0, 10))
        
        self.download_button = tk.Button(controls_container, text="Download Video", 
                                       command=self.download_video_threaded,
                                       bg=self.accent_color, fg='white', 
                                       font=('Arial', 10, 'bold'),
                                       relief=tk.FLAT, bd=0, cursor='hand2',
                                       activebackground='#2ea043',
                                       padx=15, pady=8, width=15)
        self.download_button.pack()
        
        # Progress Section (BELOW both sections)
        progress_section = tk.Frame(bottom_inner, bg=self.card_color)
        progress_section.pack(fill=tk.X, pady=(10, 0))
        
        # Progress bar section
        progress_label = tk.Label(progress_section, text="Download Progress:", 
                                font=('Arial', 11, 'bold'), 
                                bg=self.card_color, fg=self.text_color)
        progress_label.pack(anchor=tk.W, pady=(0, 5))
        
        # Progress bar frame
        progress_bar_frame = tk.Frame(progress_section, bg=self.card_color)
        progress_bar_frame.pack(fill=tk.X, pady=(0, 5))
        
        # Custom progress bar using Canvas
        self.progress_canvas = tk.Canvas(progress_bar_frame, height=20, bg=self.input_bg, 
                                       highlightbackground=self.border_color, highlightthickness=1)
        self.progress_canvas.pack(fill=tk.X, side=tk.LEFT, padx=(0, 10))
        
        self.progress_text = tk.Label(progress_bar_frame, text="0%", 
                                    font=('Arial', 10, 'bold'), 
                                    bg=self.card_color, fg=self.text_color, width=6)
        self.progress_text.pack(side=tk.RIGHT)
        
        # Status label
        self.status_label = tk.Label(progress_section, text="Ready to download", 
                                   font=('Arial', 10), 
                                   bg=self.card_color, fg=self.muted_text)
        self.status_label.pack(anchor=tk.W)
        
    def update_progress_bar(self, percentage):
        """Update the custom progress bar"""
        self.progress_canvas.delete("all")
        canvas_width = self.progress_canvas.winfo_width()
        canvas_height = self.progress_canvas.winfo_height()
        
        if canvas_width > 1:  # Make sure canvas is initialized
            progress_width = (canvas_width - 4) * (percentage / 100)
            
            # Background
            self.progress_canvas.create_rectangle(2, 2, canvas_width-2, canvas_height-2, 
                                                fill=self.input_bg, outline="")
            
            # Progress fill
            if progress_width > 0:
                self.progress_canvas.create_rectangle(2, 2, progress_width+2, canvas_height-2, 
                                                    fill=self.accent_color, outline="")
            
            # Update percentage text
            self.progress_text.config(text=f"{percentage:.1f}%")
    
    def set_initial_example_text(self):
        self.formats_text.config(state=tk.NORMAL)
        self.formats_text.delete(1.0, tk.END)
        
        initial_text = """USAGE GUIDE:

        1. Enter a YouTube URL above
        2. Click 'Fetch Formats' to get available formats
        3. Choose a format code from the right panel
        4. Enter the format code and download

        COMMON FORMAT TYPES:
        • Video + Audio: 18, 22 (complete files)
        • Video Only: 133, 134, 135, 136, 137
        • Audio Only: 140, 249, 250

        QUALITY GUIDE:
        • 144p: Format code = 160
        • 240p: Format code = 133  
        • 360p: Format code = 134
        • 480p: Format code = 135
        • 720p: Format code = 136
        • 1080p: Format code = 137

        COMBINING FORMATS:
        You can combine video and audio using '+':
        • Best 1080p: 137+140
        • Best 720p: 136+140
        • Best 480p: 135+140

        TIPS:
        • Higher format numbers = better quality
        • Larger file sizes for higher quality
        • Audio-only downloads use less bandwidth
        • Check file size before downloading

        RECOMMENDED FORMATS:
        • High Quality: 137+140 (1080p+audio)
        Under Development might not work.!
        • Balanced: 136+140 (720p+audio)  
        • Quick: 22 (720p with audio)
        • Audio Only: 140 (best audio)

    Enter the format code and click Download!"""
        
        self.formats_text.insert(tk.END, initial_text)
        self.formats_text.config(state=tk.DISABLED)
    
    def fetch_formats_threaded(self):
        # Disable button and update status
        self.fetch_button.configure(state='disabled', text='Fetching...')
        self.status_label.config(text="Fetching video information...")
        
        # Run in separate thread to prevent GUI freezing
        thread = threading.Thread(target=self.display_formats)
        thread.daemon = True
        thread.start()
    
    def display_formats(self):
        try:
            url = self.url_entry.get().strip()
            if not url:
                self.root.after(0, lambda: messagebox.showerror("Error", "Please enter a valid YouTube URL"))
                return
                
            formats_dict, video_title = video_formats(url)
            if not formats_dict:
                self.root.after(0, lambda: messagebox.showerror("Error", "No formats available or an error occurred."))
                return

            # Update UI in main thread
            self.root.after(0, lambda: self.update_format_display(formats_dict, url, video_title))
            
        except Exception as e:
            error_msg = f"An error occurred: {str(e)}"
            self.root.after(0, lambda: messagebox.showerror("Error", error_msg))
        finally:
            # Re-enable button and update status
            self.root.after(0, lambda: self.fetch_button.configure(state='normal', text='Fetch Formats'))
            self.root.after(0, lambda: self.status_label.config(text="Ready to download"))
    
    def update_format_display(self, formats_dict, url, video_title):
        # Update video title with proper formatting
        self.video_title = video_title or "Unknown Title"
        self.video_title_display.config(text=self.video_title, fg=self.text_color)
        
        # Update format details tab.
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        
        for format_id, format_info in formats_dict.items():
            self.text_area.insert(tk.END, f"FORMAT ID: {format_id}\n")
            for key, value in format_info.items():
                self.text_area.insert(tk.END, f"  {key}: {value}\n")
            self.text_area.insert(tk.END, "\n")
        
        self.text_area.config(state=tk.DISABLED)
        
        # Update examples section with specific data
        self.formats_text.config(state=tk.NORMAL)
        self.formats_text.delete(1.0, tk.END)
        
        example_data = f"""[youtube] Video information fetched!

            AVAILABLE FORMATS SUMMARY:
            Format  Ext   Resolution  Quality    Size
            249     webm  audio only  tiny       ~2MB
            250     webm  audio only  tiny       ~3MB  
            140     m4a   audio only  medium     ~5MB
            160     mp4   254x144     144p       ~10MB
            133     mp4   426x240     240p       ~20MB
            134     mp4   640x360     360p       ~30MB
            135     mp4   854x480     480p       ~50MB
            136     mp4   1280x720    720p       ~80MB
            137     mp4   1920x1080   1080p      ~150MB
            18      mp4   640x360     360p+audio ~40MB
            22      mp4   1280x720    720p+audio ~120MB

            HOW TO USE:
            1. Pick a format ID from the right panel
            2. For video+audio combo: use 137+140
            3. For audio only: use 140
            4. For quick download: use 18 or 22

            RECOMMENDED COMBINATIONS:
            • High Quality: 137+140 (1080p+audio)
            Under Development might not work.!
            • Balanced: 136+140 (720p+audio)  
            • Quick: 22 (720p with audio)
            • Audio Only: 140 (best audio)

            POPULAR FORMATS:
            • 22: 720p MP4 with audio (recommended)
            • 18: 360p MP4 with audio (fast download)
            • 140: Audio only M4A (music/podcasts)
            • 137: 1080p video only (needs +140 for audio)

        Enter the format code in the bottom section and click Download!"""
        
        self.formats_text.insert(tk.END, example_data)
        self.formats_text.config(state=tk.DISABLED)
    
    def download_video_threaded(self):
        # Disable button and update status
        self.download_button.configure(state='disabled', text='Downloading...')
        self.status_label.config(text="Starting download...")
        self.update_progress_bar(0)
        
        # Run in separate thread
        thread = threading.Thread(target=self.download_video)
        thread.daemon = True
        thread.start()
    
    def download_video(self):
        try:
            url = self.url_entry.get().strip()
            format_v = self.format_entry.get().strip()
            
            if not url or not format_v:
                self.root.after(0, lambda: messagebox.showerror("Error", "Please enter both URL and format code"))
                return
            
            # Simulate progress updates.
            for i in range(0, 101, 10):
                self.root.after(0, lambda p=i: self.update_progress_bar(p))
                self.root.after(0, lambda p=i: self.status_label.config(text=f"Downloading... {p}%"))
                threading.Event().wait(0.2)  # Simulated delay
            
            if current_os == "Windows":
                result = cmd.run(["cmd", "/c", "yt-dlp", "-f", f"{format_v}", f"{url}"], 
                               capture_output=True, text=True)
            elif current_os == "Linux":
                result = cmd.run(["yt-dlp", "-f", f"{format_v}", f"{url}"], 
                               capture_output=True, text=True)
            else:
                self.root.after(0, lambda: messagebox.showerror("Error", "Unsupported platform"))
                return
            
            if result.returncode == 0:
                self.root.after(0, lambda: self.update_progress_bar(100))
                self.root.after(0, lambda: self.status_label.config(text="Download completed successfully!"))
                self.root.after(0, lambda: messagebox.showinfo("Success", "Video downloaded successfully!"))
            else:
                error_msg = result.stderr if result.stderr else "Download failed"
                self.root.after(0, lambda: self.status_label.config(text="Download failed"))
                self.root.after(0, lambda: messagebox.showerror("Download Error", error_msg))
                
        except Exception as e:
            error_msg = f"An error occurred during download: {str(e)}"
            self.root.after(0, lambda: self.status_label.config(text="Download error occurred"))
            self.root.after(0, lambda: messagebox.showerror("Error", error_msg))
        finally:
            # Re-enable button
            self.root.after(0, lambda: self.download_button.configure(state='normal', text='Download Video'))

if __name__ == "__main__":
    OS_platform_verify()
    
    root = tk.Tk()
    app = Tubit(root)
    root.mainloop()