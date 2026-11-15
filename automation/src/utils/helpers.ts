/**
 * Trình sinh dữ liệu động và công cụ hỗ trợ kiểm thử theo chuẩn Pillar 5
 * CẤM: Điền ngày tháng gán cứng dạng YYYY-MM-DD
 */

export class Helpers {
  /**
   * Lấy ngày hôm nay theo định dạng mong muốn
   */
  static getToday(format: 'YYYY/MM/DD' | 'YYYY-MM-DD' = 'YYYY/MM/DD'): string {
    const now = new Date();
    const yyyy = now.getFullYear();
    const mm = String(now.getMonth() + 1).padStart(2, '0');
    const dd = String(now.getDate()).padStart(2, '0');
    return format === 'YYYY/MM/DD' ? `${yyyy}/${mm}/${dd}` : `${yyyy}-${mm}-${dd}`;
  }

  /**
   * Lấy ngày tương lai (+offsetDays)
   */
  static getFutureDate(offsetDays: number, format: 'YYYY/MM/DD' | 'YYYY-MM-DD' = 'YYYY/MM/DD'): string {
    const target = new Date();
    target.setDate(target.getDate() + offsetDays);
    const yyyy = target.getFullYear();
    const mm = String(target.getMonth() + 1).padStart(2, '0');
    const dd = String(target.getDate()).padStart(2, '0');
    return format === 'YYYY/MM/DD' ? `${yyyy}/${mm}/${dd}` : `${yyyy}-${mm}-${dd}`;
  }

  /**
   * Lấy ngày quá khứ (-offsetDays)
   */
  static getPastDate(offsetDays: number, format: 'YYYY/MM/DD' | 'YYYY-MM-DD' = 'YYYY/MM/DD'): string {
    const target = new Date();
    target.setDate(target.getDate() - offsetDays);
    const yyyy = target.getFullYear();
    const mm = String(target.getMonth() + 1).padStart(2, '0');
    const dd = String(target.getDate()).padStart(2, '0');
    return format === 'YYYY/MM/DD' ? `${yyyy}/${mm}/${dd}` : `${yyyy}-${mm}-${dd}`;
  }

  /**
   * Sinh chuỗi ngẫu nhiên duy nhất chống trùng lặp DB (Idempotency)
   */
  static generateUniqueString(prefix: string = 'test'): string {
    const timestamp = Date.now();
    const random = Math.floor(Math.random() * 1000);
    return `${prefix}_${timestamp}_${random}`;
  }

  /**
   * Sleep an toàn khi bắt buộc phải chờ animation hoàn tất (chỉ dùng giới hạn)
   */
  static async sleep(ms: number): Promise<void> {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }
}
