#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Ref-Util-XS
Version  : 0.117
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/Ref-Util-XS-0.117.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/Ref-Util-XS-0.117.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libr/libref-util-xs-perl/libref-util-xs-perl_0.117-1.debian.tar.xz
Summary  : 'XS implementation for Ref::Util'
Group    : Development/Tools
License  : MIT
Requires: perl-Ref-Util-XS-lib = %{version}-%{release}
Requires: perl-Ref-Util-XS-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Ref-Util-XS,
version 0.117:
XS implementation for Ref::Util

%package dev
Summary: dev components for the perl-Ref-Util-XS package.
Group: Development
Requires: perl-Ref-Util-XS-lib = %{version}-%{release}
Provides: perl-Ref-Util-XS-devel = %{version}-%{release}

%description dev
dev components for the perl-Ref-Util-XS package.


%package lib
Summary: lib components for the perl-Ref-Util-XS package.
Group: Libraries
Requires: perl-Ref-Util-XS-license = %{version}-%{release}

%description lib
lib components for the perl-Ref-Util-XS package.


%package license
Summary: license components for the perl-Ref-Util-XS package.
Group: Default

%description license
license components for the perl-Ref-Util-XS package.


%prep
%setup -q -n Ref-Util-XS-0.117
cd ..
%setup -q -T -D -n Ref-Util-XS-0.117 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Ref-Util-XS-0.117/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Ref-Util-XS
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Ref-Util-XS/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Ref/Util/XS.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Ref::Util::XS.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Ref/Util/XS/XS.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Ref-Util-XS/LICENSE
