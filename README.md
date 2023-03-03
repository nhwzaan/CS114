<!-- Banner -->
<p align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" style="border: none;">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology">
  </a>
</p>

<!-- Title -->
<h1 align="center"><b>CS114.N11.KHCL - MÁY HỌC - MACHINE LEARNING</b></h1>


## BẢNG MỤC LỤC
* [Giới thiệu môn học](#giới-thiệu-môn-học)
* [Giới thiệu nhóm](#giới-thiệu-nhóm)
* [Thư mục bài tập](#thư-mục-bài-tập-tuần)
* [Đồ án môn học](#đồ-án-môn-học)
<!--* [Tổng kết môn học](https://github.com/.../CS112.L21/blob/main/SummaryReport)-->


## GIỚI THIỆU MÔN HỌC
* **Tên môn học:** MÁY HỌC - MACHINE LEARNING
* **Mã môn học:** CS114
* **Mã lớp:** CS114.N11.KHCL
* **Năm học:** HK1 (2022 - 2023)
* **Giảng viên:** 
   1. PGS. Lê Đình Duy - *duyld@uit.edu.vn*
   2. ThS. Phạm Nguyễn Trường An - *anpnt@uit.edu.vn*

## GIỚI THIỆU NHÓM
| STT | Họ tên | MSSV | Vai trò | Email | Github | Facebook |
| :---: | --- | --- | --- | --- | --- | --- |
| 1 | Nguyễn Thị Như Vân | 20520855 | Nhóm trưởng | 20520855@gm.uit.edu.vn | [nhwzaan](https://github.com/nhwzaam) | [vanntn](https://www.facebook.com/xxnhwzaan/) |
| 2 | Phạm Bùi Nhật Huy | 20521410 | Thành viên | 20521410@gm.uit.edu.vn | [mysteryrune](https://github.com/MysteryRune) | [huypbn](https://www.facebook.com/huy.phambuinhat/) |
| 3 | Nguyễn Văn Hoàng | 20521346 | Thành viên | 20521346@gm.uit.edu.vn | [Hoangcurly1305](https://github.com/Hoangcurly1305) | [hoangnv](https://www.facebook.com/curly.uit) |

## THƯ MỤC BÀI TẬP
[1. WeCode](https://github.com/nhwzaan/CS114/tree/main/Wecode%20Exercises)

[2. Google Classroom](https://github.com/nhwzaan/CS114/tree/main/Google%20Classroom%20Exercises)

## ĐỒ ÁN MÔN HỌC
* **Chủ đề:** **IMAGE CAPTION GENERATOR - SINH MÔ TẢ CHO ẢNH**

**1.   Vấn đề đồ án đặt ra:**

Image Caption Generator tập trung vào việc tạo ra mô tả văn bản cho các hình ảnh, giúp cho việc hiểu nội dung của hình ảnh trở nên dễ dàng hơn và thuận tiện hơn cho con người. Để làm được điều này, Image Caption Generator sử dụng các mô hình học sâu để phân tích và học các đặc trưng của hình ảnh, sau đó sử dụng các mô hình ngôn ngữ để tạo ra mô tả văn bản cho hình ảnh đó.

**2.   Ứng dụng:**

Image Caption Generator được sử dụng để tạo ra mô tả văn bản cho các hình ảnh, giúp cho việc hiểu nội dung của chúng trở nên thuận tiện và dễ dàng hơn đối với con người:
- Trong Giáo dục: có thể được sử dụng trong giáo dục để giúp các học sinh và sinh viên hiểu các khái niệm và thông tin trong sách giáo khoa hoặc các tài liệu học tập bằng cách cung cấp mô tả chi tiết về hình ảnh. 
- Trong truyền thông: có thể được sử dụng trong truyền thông để tạo ra các mô tả cho các hình ảnh trong báo chí, tạp chí, trang web và các trang mạng xã hội.
- Trong công nghệ: có thể được sử dụng trong việc phát triển các ứng dụng công nghệ mới, ví dụ như trong lĩnh vực nhận diện hình ảnh hoặc xử lý dữ liệu hình ảnh tự động.

 ***Các ứng dụng cụ thể của Image Caption Generator trong thực tế:***
 
Hiện nay, có nhiều phần mềm Image Caption Generator được phát triển để tự động tạo ra các câu mô tả hình ảnh dựa trên nội dung của ảnh. Một số phần mềm Image Caption Generator nổi bật hiện nay bao gồm:

- Google Cloud Vision API: Đây là một dịch vụ của Google cung cấp các công cụ để phân tích ảnh và tạo ra các câu mô tả hình ảnh dựa trên nội dung của ảnh. Google Cloud Vision API sử dụng các mô hình Deep Learning để phân tích ảnh và tạo ra các câu mô tả.
- [Microsoft Computer Vision API](https://learn.microsoft.com/vi-vn/azure/cognitive-services/computer-vision/concept-describing-images?tabs=3-2 ): Đây là một dịch vụ của Microsoft cung cấp các công cụ để phân tích hình ảnh và tạo ra các câu mô tả hình ảnh dựa trên nội dung của ảnh. Microsoft Computer Vision API cũng sử dụng các mô hình Deep Learning để phân tích hình ảnh và tạo ra các câu mô tả
- IBM Watson Visual Recognition: Đây là một dịch vụ của IBM cung cấp các công cụ để phân tích hình ảnh và tạo ra các câu mô tả hình ảnh dựa trên nội dung của ảnh. IBM Watson Visual Recognition sử dụng các mô hình Deep Learning và các kỹ thuật Trí tuệ nhân tạo khác để phân tích hình ảnh.
- Google Image Search: là công cụ tìm kiếm hình ảnh của Google cho phép người dùng tìm các ảnh có liên quan đến một ảnh đầu vào, công cụ này được hỗ trợ bởi cơ chế truy xuất hình ảnh dựa trên nội dung (content-based image retrieval hay CBIR). Và “nội dung” ở đây có thể là màu sắc, hình dạng, kết cấu hoặc các thông tin khác được chứa đựng trong hình ảnh.

**3. Input - output:**
- Input: một bức ảnh bất kì
- Output: câu văn bản mô tả nội dung bức ảnh
  
  ![](https://github.com/nhwzaan/CS114/blob/main/images%20and%20materials/input-output.png)

**4.   Dữ liệu :**

Bộ dữ liệu [Flickr_8k](https://www.kaggle.com/datasets/adityajn105/flickr8k) bao gồm 8091 hình ảnh được lấy từ trang web Flickr và mỗi hình ảnh được kèm theo một phần mô tả văn bản. Các mô tả được đánh nhãn bởi con người để đảm bảo tính chính xác của dữ liệu. Bộ dữ liệu này được thu thập bởi một nhóm nghiên cứu tại Đại học Carnegie Mellon vào năm 2011 và công bố vào năm 2012. Quá trình thu thập và đánh nhãn này đã mất khoảng hai năm để hoàn thành. Nhóm chúng em đã sử dụng lại bộ dữ liệu này từ trang Kaggle 

**5.   Mô hình máy học:**

Nhóm chúng em sử dụng (CNN) để trích xuất tính năng hình ảnh và (LSTM) để xử lý ngôn ngữ tự nhiên (NLP).
CNN được sử dụng để trích xuất đặc trưng của ảnh, trong khi RNN được sử dụng để sử lý chuỗi (trong đồ án này chúng em sử dụng LSTM).
* ***Model creation:***
  
![](https://github.com/nhwzaan/CS114/blob/main/images%20and%20materials/model_creation.png)

* ***Pipeline:***

![](https://github.com/nhwzaan/CS114/blob/main/images%20and%20materials/pipeline.png)
    
**6.   Độ đo sử dụng:**

Trong đồ án lần này, nhóm xin được giới thiệu một độ đo để đánh giá cho bài toán này, đó là BLEU score. BLEU score (viết tắt của Bilingual Evaluation Understudy), được giới thiệu lần đầu trong bài báo khoa học [‘BLEU: a Method for Automatic Evaluation of Machine Translation’](https://aclanthology.org/P02-1040.pdf). BLEU được thiết kế để sử dụng trong dịch máy (Machine Translation), đồng thời, phép đo này cũng được sử dụng trong các nhiệm vụ như tóm tắt văn bản, nhận dạng giọng nói, sinh nhãn ảnh (image captioning). BLEU đánh giá một câu thông qua so khớp giữa câu đó và câu mẫu. Điểm được cho nằm trong khoảng 0 (sai hoàn toàn) đến 1 (khớp hoàn toàn). Cách tính của BLEU là đếm số n-gram khớp nhau giữa câu mẫu (R) và câu được đánh giá (C) sau đó chia cho số token của C. Việc chọn n phụ thuộc vào ngôn ngữ, nhiệm vụ và mục tiêu cụ thể..

Bên cạnh đó, CIDEr (Consensus-based Image Description Evaluation) là một độ đo đánh giá chất lượng mô tả hình ảnh. Nó được đề xuất trong bài báo ['CIDEr: Consensus-based Image Description Evaluation'](https://arxiv.org/abs/1411.5726) (Vedantam et al., 2015). CIDEr tính điểm bằng cách so sánh các câu mô tả được tạo bởi mô hình với các câu mô tả thực tế được đánh giá bởi con người.

*Một số độ đo khác mà nhóm có tìm hiểu:*
  - METEOR: Đánh giá thông qua matching các Uni-gram và cho ra Unigram precision, Uni-gram recall,…  Đánh giá đơn giản nhưng không đảm bảo về mặt ý nghĩa và trôi chảy của câu văn.
  - ROUGE: Đánh giá thông qua matching các overlap_word giữa 2 đoạn văn bản. Đảm bảo thứ tự của các từ khi xét so với BLEU-score và METEOR nhưng vẫn chưa giải quyết được vấn đề trôi chảy và mạch lạc của câu văn.

**7. Kết quả đánh giá:**

Xét trên cùng một tập dataset:

  - Kết quả cao nhất của bài toán trên Kaggle là: BLEU-1 : 0.53 , BLEU-2 : 0.31
  - Kết quả cao nhất của nhóm đạt được là : BLEU-1 : 0.56, BLEU-2 : 0.33
  
***Chi tiết đồ án:*** code, trained model, report [tại đây](https://github.com/nhwzaan/CS114/tree/main/Final%20Project)

