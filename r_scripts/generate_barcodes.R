# 加载必要的包
if (!require("DNABarcodes")) {
  install.packages("DNABarcodes")
}
library(DNABarcodes)

#' 生成DNA条形码
#' @param length 条形码长度
#' @param n 需要生成的条形码数量
#' @param dist 最小汉明距离
#' @return 条形码序列列表
generate_dna_barcodes <- function(length, n, dist) {
  barcodes <- tryCatch({
    create.dnabarcodes(
      n = n,
      dist = dist,
      length = length,
      metric = "hamming",
      cores = 1
    )
  }, error = function(e) {
    stop("无法生成条形码，请检查参数(长度 / 数量 / 最小距离) 是否合理：", e$message, call. = FALSE)
  })
  
  # 如果 barcodes 的长度小于 n，说明无法满足需求
  if (length(barcodes) < n) {
    stop("DNABarcodes 无法生成足够数量的条形码，请降低最小距离或减少条形码数量/长度。", call. = FALSE)
  }
  
  # 转换为字符向量
  return(as.character(barcodes))
}

#' 将条形码保存到文件
#' @param barcodes 条形码序列
#' @param filepath 输出文件路径
save_barcodes <- function(barcodes, filepath) {
  write.table(
    barcodes,
    file = filepath,
    row.names = FALSE,
    col.names = FALSE,
    quote = FALSE
  )
} 