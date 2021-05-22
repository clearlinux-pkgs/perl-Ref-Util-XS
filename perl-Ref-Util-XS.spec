#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Ref-Util-XS
Version  : 0.117
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/Ref-Util-XS-0.117.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/Ref-Util-XS-0.117.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libr/libref-util-xs-perl/libref-util-xs-perl_0.117-1.debian.tar.xz
Summary  : 'XS implementation for Ref::Util'
Group    : Development/Tools
License  : MIT
Requires: perl-Ref-Util-XS-license = %{version}-%{release}
Requires: perl-Ref-Util-XS-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Ref-Util-XS,
version 0.117:
XS implementation for Ref::Util

%package dev
Summary: dev components for the perl-Ref-Util-XS package.
Group: Development
Provides: perl-Ref-Util-XS-devel = %{version}-%{release}
Requires: perl-Ref-Util-XS = %{version}-%{release}

%description dev
dev components for the perl-Ref-Util-XS package.


%package license
Summary: license components for the perl-Ref-Util-XS package.
Group: Default

%description license
license components for the perl-Ref-Util-XS package.


%package perl
Summary: perl components for the perl-Ref-Util-XS package.
Group: Default
Requires: perl-Ref-Util-XS = %{version}-%{release}

%description perl
perl components for the perl-Ref-Util-XS package.


%prep
%setup -q -n Ref-Util-XS-0.117
cd %{_builddir}
tar xf %{_sourcedir}/libref-util-xs-perl_0.117-1.debian.tar.xz
cd %{_builddir}/Ref-Util-XS-0.117
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Ref-Util-XS-0.117/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Ref-Util-XS
cp %{_builddir}/Ref-Util-XS-0.117/LICENSE %{buildroot}/usr/share/package-licenses/perl-Ref-Util-XS/d18e6ab3560144c16a98150b92ed5703c1952029
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Ref-Util-XS/e4953dfdcc75727e91a58bf3adbd4d2aa733dfda
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Ref::Util::XS.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Ref-Util-XS/d18e6ab3560144c16a98150b92ed5703c1952029
/usr/share/package-licenses/perl-Ref-Util-XS/e4953dfdcc75727e91a58bf3adbd4d2aa733dfda

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Ref/Util/XS.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Ref/Util/XS/XS.so
