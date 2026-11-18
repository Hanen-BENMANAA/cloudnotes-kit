resource "aws_s3_bucket" "notes" {
  bucket = "cloudnotes-data"
}

resource "aws_s3_bucket_acl" "notes" {
  bucket = aws_s3_bucket.notes.id
  acl    = "public-read"   # DEFAUT VOLONTAIRE
}
