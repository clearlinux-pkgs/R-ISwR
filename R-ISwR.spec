#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: fbbd4e3
#
Name     : R-ISwR
Version  : 2.0.10
Release  : 53
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/ISwR_2.0-10.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/ISwR_2.0-10.tar.gz
Summary  : Introductory Statistics with R
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
P. Dalgaard (2008), `Introductory Statistics with R', 2nd ed., Springer Verlag, ISBN 978-0387790534.

%prep
%setup -q -n ISwR
pushd ..
cp -a ISwR buildavx2
popd
pushd ..
cp -a ISwR buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1742761786

%install
export SOURCE_DATE_EPOCH=1742761786
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ISwR/DESCRIPTION
/usr/lib64/R/library/ISwR/INDEX
/usr/lib64/R/library/ISwR/Meta/Rd.rds
/usr/lib64/R/library/ISwR/Meta/data.rds
/usr/lib64/R/library/ISwR/Meta/features.rds
/usr/lib64/R/library/ISwR/Meta/hsearch.rds
/usr/lib64/R/library/ISwR/Meta/links.rds
/usr/lib64/R/library/ISwR/Meta/nsInfo.rds
/usr/lib64/R/library/ISwR/Meta/package.rds
/usr/lib64/R/library/ISwR/NAMESPACE
/usr/lib64/R/library/ISwR/R/ISwR
/usr/lib64/R/library/ISwR/R/ISwR.rdb
/usr/lib64/R/library/ISwR/R/ISwR.rdx
/usr/lib64/R/library/ISwR/data/Rdata.rdb
/usr/lib64/R/library/ISwR/data/Rdata.rds
/usr/lib64/R/library/ISwR/data/Rdata.rdx
/usr/lib64/R/library/ISwR/help/AnIndex
/usr/lib64/R/library/ISwR/help/ISwR.rdb
/usr/lib64/R/library/ISwR/help/ISwR.rdx
/usr/lib64/R/library/ISwR/help/aliases.rds
/usr/lib64/R/library/ISwR/help/paths.rds
/usr/lib64/R/library/ISwR/html/00Index.html
/usr/lib64/R/library/ISwR/html/R.css
/usr/lib64/R/library/ISwR/rawdata/fake.trypsin.R
/usr/lib64/R/library/ISwR/rawdata/secretin.txt
/usr/lib64/R/library/ISwR/rawdata/stroke.csv
/usr/lib64/R/library/ISwR/rawdata/thuesen.txt
/usr/lib64/R/library/ISwR/scripts/ch01.R
/usr/lib64/R/library/ISwR/scripts/ch02.R
/usr/lib64/R/library/ISwR/scripts/ch03.R
/usr/lib64/R/library/ISwR/scripts/ch04.R
/usr/lib64/R/library/ISwR/scripts/ch05.R
/usr/lib64/R/library/ISwR/scripts/ch06.R
/usr/lib64/R/library/ISwR/scripts/ch07.R
/usr/lib64/R/library/ISwR/scripts/ch08.R
/usr/lib64/R/library/ISwR/scripts/ch09.R
/usr/lib64/R/library/ISwR/scripts/ch10.R
/usr/lib64/R/library/ISwR/scripts/ch11.R
/usr/lib64/R/library/ISwR/scripts/ch12.R
/usr/lib64/R/library/ISwR/scripts/ch13.R
/usr/lib64/R/library/ISwR/scripts/ch14.R
/usr/lib64/R/library/ISwR/scripts/ch15.R
/usr/lib64/R/library/ISwR/scripts/ch16.R
/usr/lib64/R/library/ISwR/scripts/ex01.R
/usr/lib64/R/library/ISwR/scripts/ex02.R
/usr/lib64/R/library/ISwR/scripts/ex03.R
/usr/lib64/R/library/ISwR/scripts/ex04.R
/usr/lib64/R/library/ISwR/scripts/ex05.R
/usr/lib64/R/library/ISwR/scripts/ex06.R
/usr/lib64/R/library/ISwR/scripts/ex07.R
/usr/lib64/R/library/ISwR/scripts/ex08.R
/usr/lib64/R/library/ISwR/scripts/ex09.R
/usr/lib64/R/library/ISwR/scripts/ex10.R
/usr/lib64/R/library/ISwR/scripts/ex11.R
/usr/lib64/R/library/ISwR/scripts/ex12.R
/usr/lib64/R/library/ISwR/scripts/ex13.R
/usr/lib64/R/library/ISwR/scripts/ex14.R
/usr/lib64/R/library/ISwR/scripts/ex15.R
/usr/lib64/R/library/ISwR/scripts/ex16.R
/usr/lib64/R/library/ISwR/tests/allexercises.R
/usr/lib64/R/library/ISwR/tests/allexercises.Rout.save
/usr/lib64/R/library/ISwR/tests/allscripts.R
/usr/lib64/R/library/ISwR/tests/allscripts.Rout.save
