import os
import random
import string
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk  # 添加导入 Image 和 ImageTk
import ffmpeg

# 设置 FFmpeg 路径
ffmpeg_path = r"C:\Users\67067\Desktop\ffmpeg-2023-08-20-git-f0b1cab538-full_build\bin"
os.environ["PATH"] += os.pathsep + ffmpeg_path  # 添加 FFmpeg 路径到环境变量

def random_folder_name(length=8):
    """生成随机文件夹名称"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def merge_images_to_video(image_paths, output_path, duration_per_frame=3):
    """将图像合并成视频"""
    # 生成 file_list.txt
    file_list_path = os.path.join(os.path.dirname(output_path), 'file_list.txt')
    with open(file_list_path, 'w', encoding='utf-8') as f:  # 使用 utf-8 编码
        for image_path in image_paths:
            f.write(f"file '{image_path}'\n")
            f.write(f"duration {duration_per_frame}\n")
        
        # 添加最后一张图片及其持续时间
        f.write(f"file '{image_paths[-1]}'\n")
        f.write(f"duration {duration_per_frame}\n")  # 确保最后一帧也有持续时间

    # 使用 ffmpeg-python 合成视频
    try:
        (
            ffmpeg
            .input(file_list_path, format='concat', safe=0)
            .output(output_path, vcodec='libx264', r=25, filter_complex='scale=iw-mod(iw\\,2):ih-mod(ih\\,2)')  # 设置帧率为25
            .run(overwrite_output=True)  
        )
        messagebox.showinfo("完成", f"视频已导出到: {output_path}")
    except ffmpeg.Error as e:
        print("An error occurred:", e)
        messagebox.showerror("错误", "合成视频时出错，请检查输入文件。")

def select_images():
    """选择图片文件"""
    file_paths = filedialog.askopenfilenames(title="选择图片文件", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if file_paths:
        output_directory = filedialog.askdirectory(title="选择保存视频的文件夹")
        if output_directory:
            output_file_name = f"{random_folder_name()}.mp4"
            output_file_path = os.path.join(output_directory, output_file_name)
            merge_images_to_video(file_paths, output_file_path)

            # 提示用户按回车继续
            input("按回车键继续导入图片...")  
            select_images()  # 重新调用选择图片的函数

def main():
    """主函数"""
    root = tk.Tk()
    root.title("批量图片转视频（本软件由戴戴的Linux、福建省智网云科科技有限公司提供技术支撑。https://daishenghui.club）")
    root.geometry("900x700")
    
    # 创建一个 frame 用于垂直居中放置组件
    frame = tk.Frame(root)
    frame.pack(expand=True)
    
    button_font = ("Arial", 14, "bold")
	
    # 创建选择图片按钮
    btn_select_images = tk.Button(frame, text="点击这里选择图片并导出视频", command=select_images, width=60, height=5, font=button_font)
    btn_select_images.pack(pady=20)
    
    # 添加二维码图片
    qrcode_path = os.path.join(os.path.dirname(__file__), "qrcode.jpg")	# 替换为二维码图片的实际路径
    if os.path.exists(qrcode_path):
        qr_image = Image.open(qrcode_path)
        qr_image = qr_image.resize((230, 230))  # 调整图片大小
        qr_photo = ImageTk.PhotoImage(qr_image)

        qr_label = tk.Label(frame, image=qr_photo)
        qr_label.image = qr_photo  # 保存引用以防止图片被垃圾回收
        qr_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
